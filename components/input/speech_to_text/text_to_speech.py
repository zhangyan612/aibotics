from gtts import gTTS
# import os
# from tempfile import TemporaryFile
# from time import sleep
# import pyglet
# from subprocess import call
# from pygame import mixer # Load the required library
# #
# mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
# mixer.music.load('tmp/temp.wav')
# mixer.music.play()
#

# import winsound
#
# winsound.PlaySound('D:\Work\projects\aibotics\components\input\speech_to_text\tmp/temp.wav', winsound.SND_FILENAME)


# import os
# import subprocess
# # file = os.system("start tmp/temp.wav")
# sts = subprocess.call("start tmp/temp.wav", shell=True)

# import subprocess
# def play(audio_file_path):
#     subprocess.call(["ffplay", "-nodisp", "-autoexit", audio_file_path], shell=True)
# play("tmp/temp.wav")

import sys
import subprocess
print(sys.platform)

def play_sound(file_path):
    if sys.platform == 'linux2':
        subprocess.call("start " + file_path)
    elif sys.platform == 'win32':
        # call("start tmp/temp.wav", shell=True)
        s = subprocess.Popen("start " + file_path, shell=True)

play_sound("tmp/temp.wav")



# import threading
# import time
# import subprocess
#
# stop_sound = False
# def play_alarm(file_name = "tmp/temp.wav"):
#
#     """Repeat the sound specified to mimic an alarm."""
#     while not stop_sound:
#         process = subprocess.Popen("start tmp/temp.wav", shell=True) #["afplay", file_name]
#         while not stop_sound:
#             if process.poll():
#                 break
#             time.sleep(0.1)
#         if stop_sound:
#             process.kill()
#
# def alert_after_timeout(timeout, message):
#     """After timeout seconds, show an alert and play the alarm sound."""
#     global stop_sound
#     time.sleep(timeout)
#     process = None
#     thread = threading.Thread(target=play_alarm)
#     thread.start()
#     # show_alert is synchronous, it blocks until alert is closed
#     # show_alert(message)
#
#     stop_sound = True
#     thread.join()
#
# play_alarm()

# Linux

# from wave import open as waveOpen
# from ossaudiodev import open as ossOpen
# s = waveOpen('tada.wav','rb')
# (nc,sw,fr,nf,comptype, compname) = s.getparams( )
# dsp = ossOpen('/dev/dsp','w')
# try:
#   from ossaudiodev import AFMT_S16_NE
# except ImportError:
#   from sys import byteorder
#   if byteorder == "little":
#     AFMT_S16_NE = ossaudiodev.AFMT_S16_LE
#   else:
#     AFMT_S16_NE = ossaudiodev.AFMT_S16_BE
# dsp.setparameters(AFMT_S16_NE, nc, fr)
# data = s.readframes(nf)
# s.close()
# dsp.write(data)
# dsp.close()



# import pyaudio
# import wave
#
# #define stream chunk
# chunk = 1024
#
# #open a wav format music
# f = wave.open("tmp/temp.wav")
# #instantiate PyAudio
# p = pyaudio.PyAudio()
# #open stream
# stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
#                 channels = f.getnchannels(),
#                 rate = f.getframerate(),
#                 output = True)
# #read data
# data = f.readframes(chunk)
#
# #play stream
# while data:
#     stream.write(data)
#     data = f.readframes(chunk)
#
# #stop stream
# stream.stop_stream()
# stream.close()
#
# #close PyAudio
# p.terminate()


# tts = gTTS(text='Hello How are you', lang='en')
# filename = 'tmp/temp.wav'
# tts.save(filename)
# call(filename)

# music = pyglet.media.load(filename, streaming=False)
# music.play()
#
# sleep(music.duration) #prevent from killing
# os.remove(filename) #remove temperory file

# f = TemporaryFile()
# tts.write_to_fp(f)
# # os.system(f)
# # Play f
# f.close()
