from os import environ

def load_env(environment_variable: str) -> str:
    value = environ[environment_variable]
    return value
