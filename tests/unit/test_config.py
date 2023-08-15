from infra.conf import config


def test_config():
    print(config.base_url)
    print(config.username)
    print(config.password)