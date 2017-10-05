# robot should be able to make conversation with human

import components.input.speech.speech_to_text.google_speech as speech_to_text
import components.input.speech.text_to_speech.text_to_speech as speaker
from components.input.speech.nlu.api_ai import *

# loop of listener

# parse voice to translate to text
speech_text = speech_to_text.recognize()

# send text to api to get an answer and action
answer, action = api_conversation().get_answer(speech_text)

# speak out the answer
speaker.speak(answer)

# another thread to do the action



