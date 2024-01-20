import os


def env(variable: str, backup: str = None):
    """
    Returns the environment variable if it exists, or the backup if it doesn't.
    :param variable: The environment variable to look for
    :param str: The default value
    :param backup: The backup value
    :return: The value of the environment variable if it exists, or the backup if it doesn't.
    """
    try:
        return os.environ[variable]
    except Exception:
        if backup is None:
            raise Exception(f"Environment variable {variable} not found")
        return backup
    
def get_all_by_prefix(prefix: str = "") -> dict[str, str]:
    """
    Returns all environment variables that start with the given prefix.
    :param prefix: The prefix to look for
    :return: A dictionary of the environment variables that start with the given prefix
    """
    return {k: v for k, v in os.environ.items() if k.startswith(prefix)}    