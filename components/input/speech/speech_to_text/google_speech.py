# !/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
from time import clock

def recognize():
    t0 = clock()
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("speech recognition start")
        audio = r.listen(source)
        # print(type(audio))
    t1 = clock()
    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("You said: " + r.recognize_google(audio))
        t2 = clock()
        print('recording: %s seconds, api request: %s seconds' % (t1 - t0, t2 - t1))
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return "I don't understand what you said"
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return "I cannot connect to web service"

if __name__ == "__main__":
    speech_text = recognize()
