import pickle
import pyttsx3
def z():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voice')
    print(voices)
    engine.setProperty('voice', voices[1])
    engine.say("hello world")
    engine.runAndWait()


z()