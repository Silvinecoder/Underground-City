

def create_session(timeout=None):
  """
  Creates a new session to the database. Looks up at the database details in docker-compose
  """

  return create_session_from_secret_name('database', timeout)


def create_session_from_secret_name(secret_name: str, timeout=None):  # pragma: integration
    """
    Creates a session to a database (with the given timeout) by looking up the provided secret.
    Makes use of `_create_session`
    :param timeout: Timeout in seconds. If not provided, the config timeout will be used.
    :return: A session to the database
    """
    secret = find_secret(secret_name)
    url = create_url(*get_connection_details(secret))
    return _create_session(url, timeout)
