import _pytest
from infra.conf import conf_utils


def pytest_addoption(parser):
    '''
    Adding options to pytest command line.
    :param parser:
    :return:
    '''

    group = parser.getgroup('sut')

    def add_option(key, description):
        group.addoption(
            '--' + key,
            action='store',
            dest='dest_' + key,
            default=None,
            help=description
        )
        parser.addini(key, description)

    for key in conf_utils.get_keys_with_default_values():
        add_option(key="sut_" + key, description=conf_utils.get_key_doc(key))


def set_config(pytest_config: _pytest.config.Config):
    '''
    Reading the configuration from pytest command line and ini file.
    Setting the configuration in config.py

    :param pytest_config:
    :return:
    '''

    def read_value(key: str, default: str) -> str:
        if getattr(pytest_config.option, 'dest_' + key):
            return getattr(pytest_config.option, 'dest_' + key)
        if key in pytest_config.inicfg:
            return pytest_config.inicfg[key]
        return default

    for key in conf_utils.get_keys_with_default_values():
        conf_utils.set_value(key, read_value("sut_" + key, conf_utils.get_keys_with_default_values()[key]))


def pytest_sessionstart(session):
    set_config(session.config)
