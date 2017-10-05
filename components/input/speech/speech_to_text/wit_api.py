from wit import Wit

client = Wit('PURT3OOTK3J7QN5Y2IJEUWD37PYRRJZY')
# response = client.message('how are you')
# print(response)

resp = None
with open('temp.wav', 'rb') as f:
  resp = client.speech(f, None, {'Content-Type': 'audio/wav'})
print('Yay, got Wit.ai response: ' + str(resp))
