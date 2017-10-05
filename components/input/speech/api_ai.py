import os.path
import sys
import os
import json

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai




def main():
    ai = apiai.ApiAI('4056d8f63dce40a18f26d9689c3a7e98')

    request = ai.event_request(apiai.events.Event("my_custom_event"))

    request.lang = 'en'  # optional, default value equal 'en'
    request.query = 'hi how are you'

    # request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

    response = request.getresponse()

    print (response.read())


class api_conversation():
    def __init__(self):
        self.token = '9cf1ff778b174c2394c7bada629a6cbd'#9cf1ff778b174c2394c7bada629a6cbd 4056d8f63dce40a18f26d9689c3a7e98
        self.ai = apiai.ApiAI(self.token)
        self.session_id =''

    def process_request(self, query=None, resetContexts=False, entities=None):
        if not query:
            return

        text_requset = self.ai.text_request()
        text_requset.query = query
        text_requset.resetContexts = resetContexts
        text_requset.entities = entities

        if self.session_id:
            text_requset.session_id = self.session_id

        response = text_requset.getresponse()
        res_text = json.loads(response.read().decode())
        return res_text

    def get_answer(self, query):
        res_text = self.process_request(query)
        print(res_text)

        if not self.session_id:
            self.session_id = res_text['sessionId']

        result = res_text['result']

        if 'action' in result.keys():
            action = result['action']
        else:
            action = ''

        answer = result['fulfillment']['speech']
        print(answer)
        return answer, action



if __name__ == '__main__':
    api_conversation().get_answer('hello how are you doing')
    # import components.input.speech.test_data as test
    # if 'action' in test.data.keys():
    #     print("action exist")
    # else:
    #     print("no action")



