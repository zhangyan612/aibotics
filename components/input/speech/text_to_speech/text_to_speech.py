# google text to audio
from gtts import gTTS
import sys
import subprocess
import os
import tempfile
import pipes


dir_path = os.path.dirname(os.path.realpath(__file__))

print(sys.platform)
# print(dir_path)

def text_to_audio(text, language):
    tts = gTTS(text=text, lang=language)
    filename = dir_path + "/tmp/temp.wav"
    tts.save(filename)

# text_to_audio("I am doing good how are you", "en")

# audio to speaker
def play_sound(file_path):
    if sys.platform == 'linux2':
        subprocess.call("start " + file_path)
    elif sys.platform == 'win32':
        # call("start tmp/temp.wav", shell=True)
        s = subprocess.Popen("start " + file_path, shell=True)

# play_sound("tmp/temp.wav")
def speak(text=''):
    if text:
        filename = dir_path + "/tmp/temp.wav"
        text_to_audio(text, "en")
        play_sound(filename)

def play(filename):
    # fix: Use platform-independent audio-output here
    # See issue jasperproject/jasper-client#188
    cmd = ['aplay', '-D', 'plughw:1,0', str(filename)]
    print('Executing %s', ' '.join([pipes.quote(arg) for arg in cmd]))
    with tempfile.TemporaryFile() as f:
        subprocess.call(cmd, stdout=f, stderr=f)
        f.seek(0)
        output = f.read()
        if output:
            print("Output was: '%s'", output)


if __name__ == "__main__":
    speak('Lovely, thanks.')
    # play(dir_path + "/tmp/temp.wav")


# def play_mp3(self, filename):
#     mf = mad.MadFile(filename)
#     with tempfile.NamedTemporaryFile(suffix='.wav') as f:
#         wav = wave.open(f, mode='wb')
#         wav.setframerate(mf.samplerate())
#         wav.setnchannels(1 if mf.mode() == mad.MODE_SINGLE_CHANNEL else 2)
#         # 4L is the sample width of 32 bit audio
#         wav.setsampwidth(4L)
#         frame = mf.read()
#         while frame is not None:
#             wav.writeframes(frame)
#             frame = mf.read()
#         wav.close()
#         play(f.name)


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

