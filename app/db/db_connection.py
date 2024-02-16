
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from config import get_config_params


def create_session(timeout=None):  # pragma: integration
    """
    Creates a session to the default database with the given timeout.
    Makes use of `create_url` and `_create_session`.
    :param timeout: Timeout in seconds. If not provided, the config timeout will be used.
    :return: A session to the database
    """
    config = get_config_params()
    db_config = config.get("database", {})
    
    engine = translate_engine(db_config.get("engine", ""))
    url = create_url(
        engine,
        db_config.get("username", ""),
        db_config.get("password", ""),
        db_config.get("host", ""),
        db_config.get("database_name", ""),
        db_config.get("port", ""),
        db_config.get("schema", ""),
        db_config.get("options", "")
    )
    
    return _create_session(url, timeout)


def _create_session(url, timeout=None):  # pragma: integration
    """
    Creates a session to the database. If `timeout` isn't provided, it will use the one in the config.
    :param url: Connection string to the DB.
    :param timeout: Optional timeout.
    :return: A connection to the DB.
    """
    config = get_config_params()
    connection_timeout = timeout if timeout else config.get("database", {}).get("timeout", "")
    
    obfuscated_url = ''.join(url.split(":")[:2]) + ':***@' + ''.join(url.split('@')[1])
    print(f"Connecting to {obfuscated_url} with a timeout of {connection_timeout} seconds.")
    
    engine = sqlalchemy.create_engine(url, connect_args={"connect_timeout": connection_timeout})
    
    print(f"Acquiring session")
    session = sessionmaker(bind=engine, expire_on_commit=False)()
    session.expire_on_commit = False
    print(f"Got session")

    return session


def translate_engine(engine: str) -> str:
    if engine.lower() in ["postgres", "postgresql"]:
        return "postgresql"
    elif engine.lower() in ["mysql", "mariadb", "maria"]:
        return "mysql"
    return engine.lower()


def create_url(engine: str, username: str, password: str, host: str, database: str, port: str or int = None,
               schema: str = None, options: str = None) -> str:  # pragma: unit
    
    _options = f"?{options}" if options else ""
    _schema = f"/{schema}" if schema else ""
    _port = f":{port}" if port else ""

    return f"{engine}://{username}:{password}@{host}{_port}/{database}{_schema}{_options}"
