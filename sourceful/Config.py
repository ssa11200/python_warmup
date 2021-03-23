from os import environ
from dotenv import load_dotenv
from .errors import raise_missing_env

load_dotenv()


class Config:

    __envs = ["DETECT_LANGUAGE_API_KEY", "ITUNES_URL", "SENTIMENT_URL", "LYRIC_URL"]

    @staticmethod
    def check_env():
        for env in Config.__envs:
            env_value = environ.get(env)
            if env_value == "" or env_value is None:
                raise EnvironmentError("{} variable is missing!".format(env))

    @staticmethod
    def envs(env):
        return environ.get(env)
