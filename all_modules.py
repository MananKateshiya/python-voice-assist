import speech_recognition as sr
from gtts import gTTS
from pygame import mixer
from email.message import EmailMessage
import ssl
import smtplib
from emsg import semsg

def emailfunc():
    speech = ('ok!')
    tts = gTTS(text=speech, lang='en')
    tts.save('S:\\Python projects\\TTSCache\\semail.mp3')
    # tts2 = gTTS(text='what is the email receiver?', lang='en')
    # tts2.save('S:\\Python projects\\TTSCache\\semail2.mp3')
    tts3 = gTTS(text='Message Body', lang='en')
    tts3.save('S:\\Python projects\\TTSCache\\semail3.mp3')
    mixer.init()
    mixer.music.load('S:\\Python projects\\TTSCache\\semail.mp3')
    mixer.music.play()
    # mixer.music.load('S:\\Python projects\\TTSCache\\semail2.mp3')
    # mixer.music.play()

    mixer.music.load('S:\\Python projects\\TTSCache\\semail3.mp3')
    mixer.music.play()
    ra = sr.Recognizer()
    with sr.Microphone(device_index=1) as source2:
        ra.adjust_for_ambient_noise(source2, duration=2)
        print('Speak Receiver ')
        audio = ra.listen(source2)
    rec = (ra.recognize_google(audio))
    rec = rec.replace('at the rate', '@').replace(' ', '').lower()
    print(rec)
    semsg(rec)
    