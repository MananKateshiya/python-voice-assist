from gtts import gTTS
from pygame import mixer

CACHE_PATH = "S:\\Major Project\\Coding\\TTSCache"

ask_r = gTTS(text='Do you want to change this?', lang='en')
ask_r.save(f'{CACHE_PATH}\\ask_r.mp3')
mixer.init()
mixer.music.load(f'{CACHE_PATH}\\ask_r.mp3')
mixer.music.play()