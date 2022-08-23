import speech_recognition as sr
from gtts import gTTS
from pygame import mixer
import os
import wikipedia
import pyttsx3
from email.message import EmailMessage
import ssl
import smtplib
import emsg


# import pickle
# def z():
#     engine = pyttsx3.init('sapi5')
#     voices = engine.getProperty('voice')
#     engine.setProperty('voice', voices[2])
#     engine.say("hello world")
#     engine.runAndWait()


# z()

while True:

    r = sr.Recognizer()

    with sr.Microphone(device_index=1) as source:
        # print(sr.Microphone().list_microphone_names())
        r.adjust_for_ambient_noise(source, duration=2)
        r.pause_threshold = 1
        r.energy_threshold = 300 #default (consider increasing if noisy environment)
        print('Speak Now ○ ')
        audio = r.listen(source)

    try:
        message = (r.recognize_google(audio, language='en-in'))
        print(message)

        if 'hello' in message:
            print("working")
            speech = ('Hello, you look great')
            tts = gTTS(text=speech, lang='en-in')
            tts.save('S:\\Python projects\\TTSCache\\hello.mp3')
            mixer.init()
            mixer.music.load('S:\\Python projects\\TTSCache\\hello.mp3')
            mixer.music.play()

        if 'good morning' in message:
            speech = ('Good Morning, how are you')
            tts = gTTS(text=speech, lang='en-in')
            tts.save('S:\\Python projects\\TTSCache\\morning_greeting.mp3')
            mixer.init()
            mixer.music.load(
                'S:\\Python projects\\TTSCache\\morning_greeting.mp3')
            mixer.music.play()

        if 'what is your name' in message:
            speech = ('my name is M')
            tts = gTTS(text=speech, lang='en')
            tts.save('S:\\Python projects\\TTSCache\\ok.mp3')
            mixer.init()
            mixer.music.load('S:\\Python projects\\TTSCache\\ok.mp3')
            mixer.music.play()

        if 'what is my name' in message:
            speech = ('Your name is Manan, sir')
            tts = gTTS(text=speech, lang='en')
            tts.save('S:\\Python projects\\TTSCache\\myname.mp3')
            mixer.init()
            mixer.music.load('S:\\Python projects\\TTSCache\\mdyname.mp3')
            mixer.music.play()

        if 'thank you' in message:
            speech = ('Your welcome sir')
            tts = gTTS(text=speech, lang='en')
            tts.save('S:\\Python projects\\TTSCache\\thx.mp3')
            mixer.init()
            mixer.music.load('S:\\Python projects\\TTSCache\\thx.mp3')
            mixer.music.play()

        if 'shutdown' in message:
            speech = ('shutting down')
            os.system("shutdown -s -t 5")
            tts = gTTS(text=speech, lang='en')
            tts.save('S:\\Python projects\\TTSCache\\sd.mp3')
            mixer.init()
            mixer.music.load('S:\\Python projects\\TTSCache\\sd.mp3')
            mixer.music.play()

        if 'close it' in message:
            speech = ('ok!')
            tts = gTTS(text=speech, lang='en')
            tts.save('S:\\Python projects\\TTSCache\\exit.mp3')
            mixer.init()
            mixer.music.load('S:\\Python projects\\TTSCache\\exit.mp3')
            mixer.music.play()
            exit()

        if 'send email' in message:
            speech = ('ok!')
            tts = gTTS(text=speech, lang='en')
            tts.save('S:\\Python projects\\TTSCache\\semail.mp3')
            tts2 = gTTS(text='what is the email receiver?', lang='en')
            tts2.save('S:\\Python projects\\TTSCache\\semail2.mp3')
            tts3 = gTTS(text='Message Body', lang='en')
            tts3.save('S:\\Python projects\\TTSCache\\semail3.mp3')
            mixer.init()
            mixer.music.load('S:\\Python projects\\TTSCache\\semail.mp3')
            mixer.music.play()
            mixer.music.load('S:\\Python projects\\TTSCache\\semail2.mp3')
            mixer.music.play()
            ra = sr.Recognizer()
            with sr.Microphone(device_index=1) as source2:
                ra.adjust_for_ambient_noise(source2, duration=2)
                print('Speak Receiver ')
                audio = ra.listen(source2)
            rec = (r.recognize_google(audio))
            rec = rec.replace('at the rate', '@').replace(' ', '').lower()
            print(rec)
            mixer.music.load('S:\\Python projects\\TTSCache\\semail3.mp3')
            mixer.music.play()


    except Exception as e:
        print("Could not understand")
        gTTS(text="Say that Again", lang='en')
