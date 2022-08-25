import speech_recognition as sr
from gtts import gTTS
from pygame import mixer
from email.message import EmailMessage
import ssl
import smtplib
from emsg import semsg

CACHE_PATH = "S:\\Major Project\\Coding\\TTSCache"

def emailfunc():


    #ask for receiver
    tts2 = gTTS(text='who is the Email receiver?', lang='en')
    tts2.save(f'{CACHE_PATH}\\e_rec.mp3')
    mixer.init()
    mixer.music.load(f'{CACHE_PATH}\\e_rec.mp3')
    mixer.music.play()
    ra = sr.Recognizer()
    with sr.Microphone(device_index=1) as source2:
        ra.adjust_for_ambient_noise(source2, duration=2)
        print('Speak Email Receiver ○')
        a_receiver = ra.listen(source2)
    rec = (ra.recognize_google(a_receiver))
    rec = rec.replace('at the rate', '@').replace(' ', '').lower()
    print(rec)

    #ask subject
    tts = gTTS(text='what is the Email subject?', lang='en')
    tts.save(f'{CACHE_PATH}\\e_sub.mp3')
    mixer.init()
    mixer.music.load(f'{CACHE_PATH}\\e_sub.mp3')
    mixer.music.play()
    rb = sr.Recognizer()
    with sr.Microphone(device_index=1) as source3:
        rb.adjust_for_ambient_noise(source3, duration=2)
        print('Speak Emali Subject ○')
        a_subject = rb.listen(source3)
    sub = (rb.recognize_google(a_subject)).lower()
    

    #ask body
    tts3 = gTTS(text='what is the message Body?', lang='en')
    tts3.save(f'{CACHE_PATH}\\e_body.mp3')
    mixer.init()
    mixer.music.load(f'{CACHE_PATH}\\e_body.mp3')
    mixer.music.play()
    rc = sr.Recognizer()
    with sr.Microphone(device_index=1) as source4:
        rc.adjust_for_ambient_noise(source4, duration=2)
        print('Speak Email Body ○')
        a_receiver = rc.listen(source4)
    body = (rc.recognize_google(a_receiver))
    
    #main Email logic
    print(f"From: manan.kateshiya111006@marwadiuniversity.ac.in\nTo: {rec}\nSubject: {sub} \nBody: {body}")
    semsg(rec, sub, body)
    tts3 = gTTS(text='Your Email has been sent successfully!', lang='en')
    tts3.save(f'{CACHE_PATH}\\e_success.mp3')
    mixer.init()
    mixer.music.load(f'{CACHE_PATH}\\e_success.mp3')
    mixer.music.play()

def greet():
    speech = ('Hello!')
    tts = gTTS(text=speech, lang='en')
    tts.save(f'{CACHE_PATH}\\hello.mp3')
    mixer.init()
    mixer.music.load(f'{CACHE_PATH}\\hello.mp3')
    mixer.music.play()