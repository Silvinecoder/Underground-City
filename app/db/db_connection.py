
import logging
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from app.config import get_config_params

def create_session(timeout=None):
    """
    We are creating a session with the database.
    :param timeout: How long your application should wait for a connection before taking appropriate action.
    :obfuscated_url: How the connection URL should look like.
    :engine_url: The connection URL for the given database engine.
    :engine: The database engine.
    :Session: The sessionmaker.
    :session: The session.
    """

    config = get_config_params() # We are getting our configuration parameters
    database_config = config.get("database", {})
    connection_timeout = timeout if timeout else database_config.get("timeout", 30)  # With a timeout, you can specify how long your application should wait for a connection before taking appropriate action.

    obfuscated_url = (
        f"{database_config['engine']}://{database_config['username']}:***@"
        f"{database_config['host']}:{database_config['port']}/{database_config['database_name']}"
    )
    logging.info(f"Connecting to database with: {obfuscated_url} (timeout: {connection_timeout})")

    engine_url = create_generic_url(**database_config) # We are creating a connection URL with the database_config for the given database engine
    engine = create_engine(engine_url, connect_args={"connect_timeout": connection_timeout})

    logging.debug(f"Acquiring session")
    Session = sessionmaker(bind=engine, expire_on_commit=False)
    session = Session()

    logging.debug(f"Got session")

    return session

def create_generic_url(engine, username, password, host, port, database_name, schema: str = None):
    _schema = f"/{schema}" if schema else ""
    return f"{engine}://{username}:{password}@{host}:{port}/{database_name}{_schema}"


def has_table_access(table_name: str) -> bool:  # pragma: integration
    """
    Checks if the application has access to the given table.
    :param table_name: Table to check.
    :return: Whether the table is accessible.
    """
    try:
        _SESSION.execute(text(f"select count(*) from {table_name}"))
    except Exception as e:
        logging.warning(f"Unexpected error: {e}")
        return False
    return True

_SESSION = create_session(create_generic_url)