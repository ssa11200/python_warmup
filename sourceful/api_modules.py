import requests
from .helpers import (
    get_random_integer,
    polarity_search_keword,
    do_request,
    mock_sentiment_request,
)


def find_music_for_feeling(feeling_polarity):
    polarity_degree = feeling_polarity["polarity"]
    polarity_type = feeling_polarity["type"]
    keyword = polarity_search_keword(polarity_degree, polarity_type)
    url = "https://itunes.apple.com/search?term={}&media=music".format(keyword)
    response = do_request(url, "get")
    all_musics = response["results"]
    total_musics = len(all_musics)
    random_number = get_random_integer(total_musics)
    selected_music = all_musics[random_number]
    return selected_music


# in cases this api is down please use mock_sentiment_request instead
def analyse_feeling_polarity(feeling):
    url = "https://sentim-api.herokuapp.com/api/v1/"
    body = {"text": feeling}
    response = do_request(url, "post", body=body)
    # response = mock_sentiment_request()
    polarity = response["result"]
    return polarity


def find_lyrics_for_music(music):
    artist = music["artistName"]
    music_name = music["trackName"]
    url = "https://api.lyrics.ovh/v1/{}/{}".format(artist, music_name)

    # this api does not retun a response stating that lyrics not found so that I had to handle the error like this
    try:
        response = requests.get(url, timeout=5).json()
        lyrics = response["lyrics"]
    except:
        lyrics = "Lyrics Not Found!"

    return lyrics