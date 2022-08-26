import pyttsx3

#
engine = pyttsx3.init('nsss')

# Set Rate, Volume
engine.setProperty('rate', 200)
engine.setProperty('volume', 1.0)
engine.setProperty('age', 10)

# Set Voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Default voice.


def speak(text):
    """Used to speak whatever text is passed to it"""
    engine.say(text)
    engine.runAndWait()


# Text to Speech Conversion with diff voice.
def speak(text, voice_num):
    """Used to speak whatever text is passed to it"""
    #engine.setProperty('voice', voices[voice_num].id)
    engine.say(text)
    engine.runAndWait()
