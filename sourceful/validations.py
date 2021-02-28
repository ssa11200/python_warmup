import detectlanguage


def validate_language(user_input, api_key):
    detectlanguage.configuration.api_key = api_key
    detected_languages = detectlanguage.detect(user_input)

    for language in detected_languages:
        if language["language"] == "en":
            return language["isReliable"]

    return False