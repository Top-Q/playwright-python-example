import re
from infra.conf import config


def get_key_doc(key: str) -> str:
    p = re.compile(f"{key}[\s]?:(.+)\n\s+(.+)")
    m = p.search(config.__doc__)
    if m:
        return m.group(2)


def get_keys_with_default_values() -> dict:
    default_values = {}
    for key in config.__dict__:
        if not key.startswith('__'):
            default_values[key] = config.__dict__[key]
    return default_values


def set_value(key: str, value: str):
    config.__dict__[key] = value

