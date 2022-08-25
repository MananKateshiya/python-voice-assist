import speech_recognition as sr
from gtts import gTTS
from pygame import mixer
import pyttsx3
import smtplib
from all_modules import *

# import pickle
# def z():
#     engine = pyttsx3.init('sapi5')
#     voices = engine.getProperty('voice')
#     engine.setProperty('voice', voices[2])
#     engine.say("hello world")
#     engine.runAndWait()


# z()
CACHE_PATH = "S:\\Major Project\\Coding\\TTSCache"

start = gTTS(text="This is your assistant, How can i help you?", lang='en')
start.save(f'{CACHE_PATH}\\start.mp3')
mixer.init()
mixer.music.load(f'{CACHE_PATH}\\start.mp3')
mixer.music.play()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        # print(sr.Microphone().list_microphone_names())
        r.adjust_for_ambient_noise(source, duration=2)
        # r.pause_threshold = 1
        r.energy_threshold = 300 #default (consider increasing if noisy environment)
        print('Speak Now ○ ')
        audio = r.listen(source)

        try:
            message = (r.recognize_google(audio, language='en-in'))
            print(message)
        except Exception as e:
            print(e)
            mixer.quit()
            tts = gTTS(text="Say that Again", lang='en')
            tts.save(f'{CACHE_PATH}\\say_again.mp3')
            mixer.init()
            mixer.music.load(f'{CACHE_PATH}\\say_again.mp3')
            mixer.music.play()
            return "None"
        return message

if __name__ == "__main__":

    while True:
            message = takeCommand().lower()
            if 'hello' in message:
                greet()

            # if 'good morning' in message:
            #     speech = ('Good Morning, how are you')
            #     tts = gTTS(text=speech, lang='en-in')
            #     tts.save(f'{CACHE_PATH}\\morning_greeting.mp3')
            #     mixer.init()
            #     mixer.music.load(
            #         f'{CACHE_PATH}\\morning_greeting.mp3')
            #     mixer.music.play()

            if 'what is your name' in message:
                speech = ('my name is M')
                tts = gTTS(text=speech, lang='en')
                tts.save(f'{CACHE_PATH}\\ok.mp3')
                mixer.init()
                mixer.music.load(f'{CACHE_PATH}\\ok.mp3')
                mixer.music.play()

            if 'what is my name' in message:
                speech = ('Your name is Manan, sir')
                tts = gTTS(text=speech, lang='en')
                tts.save(f'{CACHE_PATH}\\myname.mp3')
                mixer.init()
                mixer.music.load(f'{CACHE_PATH}\\mdyname.mp3')
                mixer.music.play()

            if 'thank you' in message:
                speech = ('Your welcome sir')
                tts = gTTS(text=speech, lang='en')
                tts.save(f'{CACHE_PATH}\\thx.mp3')
                mixer.init()
                mixer.music.load(f'{CACHE_PATH}\\thx.mp3')
                mixer.music.play()

            if 'shutdown' in message:
                speech = ('shutting down')
                os.system("shutdown -s -t 5")
                tts = gTTS(text=speech, lang='en')
                tts.save(f'{CACHE_PATH}\\sd.mp3')
                mixer.init()
                mixer.music.load(f'{CACHE_PATH}\\sd.mp3')
                mixer.music.play()

            if 'close it' in message:
                speech = ('ok!')
                tts = gTTS(text=speech, lang='en')
                tts.save(f'{CACHE_PATH}\\exit.mp3')
                mixer.init()
                mixer.music.load(f'{CACHE_PATH}\\exit.mp3')
                mixer.music.play()
                exit()

            if 'send email' in message:
                emailfunc()


        
