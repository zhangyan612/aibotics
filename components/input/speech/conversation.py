# robot should be able to make conversation with human

import components.input.speech.speech_to_text.google_speech as speech_to_text
import components.input.speech.text_to_speech.text_to_speech as speaker
from components.input.speech.nlu.api_ai import *

# loop of listener

# parse voice to translate to text
speech_text = speech_to_text.recognize_bing()

# send text to api to get an answer and action
answer, action = api_conversation().get_answer(speech_text)

# speak out the response
speaker.speak(answer)



# listener for voice

# another thread to do the action
# blue tooth 0A:EC:04:04:D7:38
# sudo bluez-simple-agent hci0 0A:EC:04:04:D7:38
# sudo bluez-test-device trusted 0A:EC:04:04:D7:38 yes
# /etc/init.d/bluetooth start
# /etc/init.d/bluetooth connect 0A:EC:04:04:D7:38
# hcitool scan
# sudo /etc/init.d/bluetoothctl

# sudo connect 0A:EC:04:04:D7:38
# sudo bluez-simple-agent hci0 0A:EC:04:04:D7:38
# sudo bluez-test-device trusted 0A:EC:04:04:D7:38 yes
# sudo rfcomm connect hci0 0A:EC:04:04:D7:38

