from config_helper.helpers.environment import env, get_all_by_prefix

_PREFIX = "CELIAC"
_LOG_LEVEL = "INFO"

config = {
    "log_level": env(f"{_PREFIX}_LOG_LEVEL", "INFO").upper()
}

def get_prefix():
    global _PREFIX
    return _PREFIX

def get_config_params():
    global config
    return config

def set_prefix(prefix: str):
    global _PREFIX
    _PREFIX = prefix.upper().replace("-", "_")

def get_config_params():
    global config
    return config    