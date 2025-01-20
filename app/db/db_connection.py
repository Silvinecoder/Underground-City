import logging
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from app.config import get_config_params


# Global variables for the database engine and sessionmaker
_ENGINE = None
_SESSION_MAKER = None
_SESSION = None


def initialize_engine_and_sessionmaker(timeout=None):
    """
    Initializes the database engine and sessionmaker globally.
    """
    global _ENGINE, _SESSION_MAKER

    config = get_config_params()
    database_config = config.get("database", {})
    connection_timeout = timeout or database_config.get("timeout", 30)

    obfuscated_url = (
        f"{database_config['engine']}://{database_config['username']}:***@"
        f"{database_config['host']}:{database_config['port']}/{database_config['database_name']}"
    )
    logging.info(
        f"Connecting to database with: {obfuscated_url} (timeout: {connection_timeout})"
    )

    engine_url = create_generic_url(**database_config)
    _ENGINE = create_engine(
        engine_url, connect_args={"connect_timeout": connection_timeout}
    )
    _SESSION_MAKER = sessionmaker(bind=_ENGINE, expire_on_commit=False)


def create_session():
    """
    Creates and returns a new database session.
    """
    global _SESSION_MAKER
    if not _SESSION_MAKER:
        raise RuntimeError("Engine and sessionmaker are not initialized. Call initialize_engine_and_sessionmaker first.")
    return _SESSION_MAKER()


def refresh_session():
    """
    Refreshes the global session and returns a new one.
    """
    global _SESSION
    if _SESSION:
        try:
            _SESSION.close()
        except Exception as e:
            logging.warning(f"Error while closing session: {e}")
    _SESSION = create_session()
    return _SESSION


def create_generic_url(engine, username, password, host, port, database_name, schema: str = None):
    """
    Constructs a database connection URL.
    """
    _schema = f"/{schema}" if schema else ""
    return f"{engine}://{username}:{password}@{host}:{port}/{database_name}{_schema}"


def has_table_access(table_name: str) -> bool:  # pragma: integration
    """
    Checks if the application has access to the given table.
    :param table_name: Table to check.
    :return: Whether the table is accessible.
    """
    global _SESSION
    if not _SESSION:
        raise RuntimeError("Session is not initialized. Call refresh_session first.")

    try:
        _SESSION.execute(text(f"SELECT COUNT(*) FROM {table_name}"))
    except Exception as e:
        logging.warning(f"Unexpected error while accessing table {table_name}: {e}")
        return False
    return True


# Initialize engine and sessionmaker on module load
initialize_engine_and_sessionmaker()
_SESSION = create_session()
