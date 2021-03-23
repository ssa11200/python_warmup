from os import environ
from sourceful.MusicMatcher import MusicMatcher
from sourceful.Config import Config
from sourceful.validations import validate_language


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
    Config.check_env()
    feeling_input = get_user_input()
    my_music = MusicMatcher(feeling_input)
    my_music.match_music()
    music_details = my_music.music["music_details"]
    music_lyrics = my_music.music["music_lyrics"]
    display_results(music_details, music_lyrics)
