import requests
from .helpers import (
    get_random_integer,
    polarity_search_keword,
    do_request,
    mock_sentiment_request,
)
from sourceful.Config import Config


def find_music_for_feeling(feeling_polarity):
    polarity_degree = feeling_polarity["polarity"]
    polarity_type = feeling_polarity["type"]
    keyword = polarity_search_keword(polarity_degree, polarity_type)
    query = "search?term={}&media=music".format(keyword)
    itunes_url = Config.envs("ITUNES_URL") + query
    response = do_request(itunes_url, "get")
    all_musics = response["results"]
    total_musics = len(all_musics)
    random_number = get_random_integer(total_musics)
    selected_music = all_musics[random_number]
    return selected_music


# in cases this api is down please use mock_sentiment_request instead
def analyse_feeling_polarity(feeling):
    sentiment_url = Config.envs("SENTIMENT_URL")
    body = {"text": feeling}
    response = do_request(sentiment_url, "post", body=body)
    # response = mock_sentiment_request()
    polarity = response["result"]
    return polarity


def find_lyrics_for_music(music):
    artist = music["artistName"]
    music_name = music["trackName"]
    params = "{}/{}".format(artist, music_name)
    lyric_url = Config.envs("LYRIC_URL") + params

    # this api does not retun a response stating that lyrics not found so that I had to handle the error like this
    try:
        response = requests.get(lyric_url, timeout=15).json()
        lyrics = response["lyrics"]
        # response.raise_for_status()
    except Exception as error:
        message = type(error).__name__
        print(message)
        lyrics = "Lyrics Not Found!"

    return lyrics