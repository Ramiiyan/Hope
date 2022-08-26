from decouple import config
import speak_out


user_name = config('USER')
bot_name = config('BOTNAME')

#engine = pyttsx3.init('nsss')

# Set Rate, Volume
#engine.setProperty('rate', 200)
#engine.setProperty('volume', 1.0)
#engine.setProperty('age', 10)

# Set Voice
#voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[47].id)


speak_out.speak("Good morning. It's 7 A.M.")
speak_out.speak("The weather in Malibu is 72 degrees with scattered clouds.")
speak_out.speak("The surf conditions are fair with waist to shoulder highlines, high tide will be at 10:52 a.m.")


# for i in range(47):
#     print(i)
#     speak("hello ramiyan", i)