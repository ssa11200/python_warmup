from .api_modules import (
    analyse_feeling_polarity,
    find_music_for_feeling,
    find_lyrics_for_music,
)


class MusicMatcher:
    def __init__(self, feeling):
        self.feeling = feeling
        self._music = None
        self._lyrics = None
        self._polarity = None

    def _analyse_feeling(self):
        self._polarity = analyse_feeling_polarity(self.feeling)

    def _find_music(self):
        self._music = find_music_for_feeling(self._polarity)

    def _find_lyrics(self):
        self._lyrics = find_lyrics_for_music(self._music)

    def match_music(self):
        self._analyse_feeling()
        self._find_music()
        self._find_lyrics()

    @property
    def music(self):
        return {"music_details": self._music, "music_lyrics": self._lyrics}