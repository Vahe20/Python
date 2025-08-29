import speech_recognition as sr
from vosk import KaldiRecognizer, Model
from gtts import gTTS
from playsound3 import playsound
from rapidfuzz import fuzz
import pvporcupine
import pyaudio, json
import struct
import os
import threading
import time
from rus2num import Rus2Num

import config
import commands
import gAi


sr.pause_threshold = 0.5
vosk_model = Model(config.dirPath + "/vosk-model")

porcupine = pvporcupine.create(
    access_key=config.ACCESS_KEY,
    keywords=[].copy() + config.START_WORD
)

pa = pyaudio.PyAudio()
stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length
)


def listen_vosk(phrase_time_limit=7):
    rec = KaldiRecognizer(vosk_model, 16000)
    start_time = time.time()

    while time.time() - start_time < phrase_time_limit:
        data = stream.read(4000, exception_on_overflow=False)
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            if res["text"] != "":
                return res["text"].lower()
        else:
            partial = json.loads(rec.PartialResult())
            if partial.get("partial", ""):
                pass

    return "error"

def listen_command(timeout=5, phrase_time_limit=7):
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.5)
            audio = recognizer.listen(mic, timeout=timeout, phrase_time_limit=phrase_time_limit)

            for lang in ["ru-RU", "en-US"]:
                try:
                    return recognizer.recognize_google(audio, language=lang).lower()
                except sr.UnknownValueError:
                    continue
                except sr.RequestError:
                    break
    except Exception as e:
        print("⚠️ Ошибка Google SR:", e)

    # print("🎤 Слушаю через Vosk...")
    # return listen_vosk(phrase_time_limit=phrase_time_limit)



def speak(text):
    try:
        playsound(config.sounds + "\\" + text + ".wav")
    except:
        tts = gTTS(text=text, lang="ru", slow=False)
        tts.save(config.dirPath + "\\audio.mp3")
        playsound(config.dirPath + "\\audio.mp3")
        os.remove(config.dirPath + "\\audio.mp3")


def speak_async(text):
    threading.Thread(target=speak, args=(text,), daemon=True).start()



def process_command(query: str):
    best_match = None
    best_score = 0

    for command_name, triggers in config.commands_dict['commands'].items():
        if isinstance(triggers, list):
            for trigger in triggers:
                score = fuzz.partial_ratio(trigger, query)
                if score > best_score:
                    best_score = score
                    best_match = command_name

    if best_score > 70:
        try:
            result = commands.executor(best_match)
            if result:
                speak_async(result)
        except:
            speak_async("Произошла ошибка")


def main():
    speak_async("Доброе утро")

    while True:
        pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        keyword_index = porcupine.process(pcm)
        if keyword_index >= 0:
            speak_async("Да сэр")

            start_time = time.time()
            while time.time() - start_time < 15:
                query = listen_command(timeout=2, phrase_time_limit=7)
                print(query)
                
                if query == "отключись":
                    speak("Отключаю питание")
                    return
                elif query == "спасибо":
                    speak_async("К вашим услугам сэр")
                    break
                elif query == "поиск":
                    speak_async("Да сэр")
                    query = listen_command(timeout=5, phrase_time_limit=7)
                    speak_async(gAi.ask_gpt(query))
                    break
                elif query == "таймер":
                    speak_async("Да сэр")
                    query = listen_vosk()
                    r2n = Rus2Num()
                    print(r2n(query))
                    commands.jarvis_timer(r2n(query))
                    break
                if query not in ["error", "timeout"]:
                    process_command(query)


if __name__ == "__main__":
    main()

