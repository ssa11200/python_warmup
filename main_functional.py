from os import environ
from dotenv import load_dotenv
from sourceful.api_modules import (
    find_music_for_feeling,
    find_lyrics_for_music,
    analyse_feeling_polarity,
)
from sourceful.validations import validate_language
from sourceful.helpers import check_envs

# env checking
load_dotenv()
check_envs()


def get_user_input():
    detectlanguage_api_key = environ.get("DETECT_LANGUAGE_API_KEY")

    while True:
        user_input = input("Please describe your today's feeling in few words: ")

        if not validate_language(user_input, detectlanguage_api_key):
            print("Sorry, Please be more specific")
            continue
        else:
            return user_input


def display_results(music_details, music_lyrics):
    track_name = music_details["trackName"]
    artist_name = music_details["artistName"]
    collection_name = music_details["collectionName"]
    itunes_url = music_details["trackViewUrl"]

    print(
        "\n\n This music may suit your mood: \n\n Music: {} \n\n Artist: {} \n\n Collcetion: {} \n\n On Itunes: {} \n\n Lyrics: {}".format(
            track_name, artist_name, collection_name, itunes_url, music_lyrics
        )
    )


if __name__ == "__main__":
    feeling_input = get_user_input()
    feeling_polarity = analyse_feeling_polarity(feeling_input)
    music_details = find_music_for_feeling(feeling_polarity)
    music_lyrics = find_lyrics_for_music(music_details)
    display_results(music_details, music_lyrics)
