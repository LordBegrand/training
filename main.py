import speech_recognition as sr
import gtts
from playsound import playsound
import os
from notion import NotionClient
from datetime import datetime



r = sr.Recognizer()

activate = "hey sam"
client = NotionClient(token,database_id)
def get_audio():
    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)
    return audio

def audio_to_text(audio):
    text = ""
    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Speech reccognition could not understend audio")
    except sr.RequestError:
        print("Could not request result from api")
    return text

def play_sound(text):
    try:
        tts = gtts.gTTS(text)
        tempfile = "./temp.mp3"
        tts.save(tempfile)
        playsound(tempfile)
        os.remove(tempfile)
    except AssertionError:
        print("cloud not play the sound")

if __name__ == "__main__":
    while True:
        a = get_audio()
        command = audio_to_text(a)
        if activate in command.lower():
            print("activate")
            play_sound("What can i do for u?")

            note = get_audio()
            note = audio_to_text(note)

            if note:
                play_sound(note)
                
                now = datetime.now().astimezone().isoformat()
                res = client.create_page(note, now, status="Acrive")
                if res.status_code == 200:
                    play_sound("Stored new ITEM")