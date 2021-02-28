from sys import exit


def raise_api_error(url):
    exit("Error: {} does not respond!".format(url))


def raise_body_error(url):
    exit("Error: body is missing for {} post request".format(url))


def raise_missing_env(env):
    exit("Error: {} is missing".format(env))