# robot should be able to make conversation with human

import components.input.speech.google_speech as speech_to_text
from components.input.speech.api_ai import *
import components.input.speech.text_to_speech as speaker

# loop of listener

# parse voice to translate to text
speech_text = speech_to_text.recognize()

# send text to api to get an answer and action
answer, action = api_conversation().get_answer(speech_text)

# speak out the answer
speaker.speak(answer)

# another thread to do the action



