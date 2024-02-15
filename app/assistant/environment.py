import os


def env(variable: str, backup: str = None) -> str:  # pragma: unit
    """
    The function attempts to retrieve the value of the specified environment variable using os.environ[variable].
    If the variable is defined, it returns its value.
    If the variable is not defined, it checks if a backup value is provided.
    """
    try:
        return os.environ[variable]
    except Exception:
        if backup is None:
            raise Exception(f"No backup defined for {variable}")
        return backup