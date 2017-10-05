from wit import Wit
import components.input.speech.speech_to_text.recorder as record
from time import clock

client = Wit('PURT3OOTK3J7QN5Y2IJEUWD37PYRRJZY')
# response = client.message('how are you')
# print(response)


def recognize():
  t0 = clock()
  record.record_wav()
  t1 = clock()
  resp = None
  with open('output.wav', 'rb') as f:
    resp = client.speech(f, None, {'Content-Type': 'audio/wav'})
  print('Wit.ai response: ' + str(resp))
  t2 = clock()
  print('recording: %s seconds, api request: %s seconds' %(t1-t0, t2-t1))
  return resp['_text']


if __name__ == "__main__":
  text = recognize()
  print(text)
