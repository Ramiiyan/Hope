import pyttsx3
from decouple import config

user_name = config('USER')
bot_name = config('BOTNAME')


engine = pyttsx3.init('nsss')

# Set Rate, Volume
engine.setProperty('rate', 200)
engine.setProperty('volume', 1.0)
engine.setProperty('age', 10)

# Set Voice
voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[47].id)

print(voices)


# Text to Speech Conversion
def speak(text, voice_num):
    """Used to speak whatever text is passed to it"""
    #engine.setProperty('voice', voices[voice_num].id)
    engine.say(text)
    engine.runAndWait()


speak("Good morning. It's 7 A.M. The weather in Malibu is 72 degrees with scattered clouds. The surf conditions are "
      "fair with waist to shoulder highlines, high tide will be at 10:52 a.m.", 7)

# for i in range(47):
#     print(i)
#     speak("hello ramiyan", i)


