from os import environ


ENVS = [
    "envs needed to access stuff"
]


def load_conf(app):
    for name in ENVS:
        app.config[name] = environ.get(name)
