import requests
from os import environ
from dotenv import load_dotenv
from .errors import raise_api_error, raise_body_error, raise_missing_env
from .utils import get_decimal_number, get_random_integer

load_dotenv()


def polarity_search_keword(degree, type):
    polarity_types = {
        "positive": lambda degree: "excited"
        if degree > 0 and degree <= 0.5
        else "happy",
        "negative": lambda degree: "heartbroken"
        if degree > 0 and degree <= 0.5
        else "sad",
        "neutral": lambda degree: "unhappy"
        if degree > 0 and degree <= 0.5
        else "unfortunate",
    }

    return polarity_types[type](degree)


def do_request(url, method, **options):
    time_out = options["time_out"] if "time_out" in options else 10
    body = options["body"] if "body" in options and method is "post" else None

    if method == "post" and body is None:
        raise_body_error(url)

    # javascript case/switch statement mimic
    response_method_switch = {
        "get": lambda: requests.get(url, timeout=time_out).json(),
        "post": lambda: requests.post(url, json=body, timeout=time_out).json(),
        "default": lambda: requests.get(url, timeout=time_out).json(),
    }

    try:
        default_switch_function = response_method_switch["default"]
        response = response_method_switch.get(method, default_switch_function)()
        return response
    except:
        # custom api error handling
        raise_api_error(url)


# mock sentiment api call in cases the api is down
def mock_sentiment_request():
    random_int = get_random_integer(3)
    possible_types = {0: "positive", 1: "negative", 2: "neutral"}
    selected_type = possible_types[random_int]
    polarity_value = get_decimal_number(0, 1)
    response = {"result": {"type": selected_type, "polarity": polarity_value}}
    return response


def check_envs():
    envs_list = ["DETECT_LANGUAGE_API_KEY"]

    for env in envs_list:
        value = environ.get(env)

        if value == "" or value is None:
            raise_missing_env(env)
