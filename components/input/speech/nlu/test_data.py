response = {'status':{'code': 200, 'errorType': 'success'},
            'lang': 'en',
            'id': '2e86a4a7-ed5f-4597-a394-a81a65edab56',
            'result': {'metadata': {},
                       'score': 1.0,
                       'action': 'smalltalk.greetings.how_are_you',
                       'source': 'domains',
                       'fulfillment': {'speech': 'Wonderful as always. Thanks for asking.',
                                       'messages': [{'type': 0,
                                                     'speech': 'Wonderful as always. Thanks for asking.',
                                                     'id': '8a3b8701-b026-4a35-909c-89446ecc1cde'}]},
                       'resolvedQuery': 'hi how are you',
                       'contexts': [],
                       'parameters': {},
                       'actionIncomplete': False
                       },
            'timestamp': '2017-10-05T16:01:08.88Z',
            'sessionId': '307ba83c004c4dff9d473198d59ca282'}

smart_home = {'lang': 'en',
              'id': 'b7500124-3465-434d-91b2-8fc2e94dbe8d',
              'status': {'code': 200, 'errorType': 'success'},
              'result': {'contexts':
                             [{'name': 'schedule', 'lifespan': 3, 'parameters': {'device.original': '', 'device': '', 'all.original': '', 'color': '', 'room.original': 'kitchen', 'room': 'kitchen', 'all': '', 'color.original': ''}},
                              {'name': 'brightness', 'lifespan': 5, 'parameters': {'device.original': '', 'device': '', 'all.original': '', 'color': '', 'room.original': 'kitchen', 'room': 'kitchen', 'all': '', 'color.original': ''}},
                              {'name': 'check', 'lifespan': 3, 'parameters': {'device.original': '', 'device': '', 'all.original': '', 'color': '', 'room.original': 'kitchen', 'room': 'kitchen', 'all': '', 'color.original': ''}},
                              {'name': 'color', 'lifespan': 3, 'parameters': {'device.original': '', 'device': '', 'all.original': '', 'color': '', 'room.original': 'kitchen', 'room': 'kitchen', 'all': '', 'color.original': ''}},
                              {'name': 'switch', 'lifespan': 3, 'parameters': {'device.original': '', 'device': '', 'all.original': '', 'color': '', 'room.original': 'kitchen', 'room': 'kitchen', 'all': '', 'color.original': ''}},
                              {'name': 'room', 'lifespan': 3, 'parameters': {'device.original': '', 'device': '', 'all.original': '', 'color': '', 'room.original': 'kitchen', 'room': 'kitchen', 'all': '', 'color.original': ''}}],
                         'score': 1.0, 'actionIncomplete': False,
                         'fulfillment': {'speech': '', 'messages': [{'id': '7ee7f87b-fbcc-4f10-a8cb-2ecd985f0bc6', 'speech': '', 'type': 0}]},
                         'action': 'smarthome.lights.switch.on',
                         'resolvedQuery': 'can you turn on the light in kitchen?',
                         'source': 'agent',
                         'metadata': {'intentName': 'smarthome.lights.switch.on', 'webhookUsed': 'false', 'webhookForSlotFillingUsed': 'false', 'intentId': 'e3acf680-4ebe-48c4-9e02-cc4c9bec5d37'},
                         'parameters': {'all': '', 'device': '', 'color': '', 'room': 'kitchen'}},
              'sessionId': '6ff6730a24e841aa836cafd56f3b1ac5',
              'timestamp': '2017-10-05T16:16:48.637Z'}


data ={'status': {'code': 200, 'errorType': 'success'}, 'id': 'bfef8bb5-748d-45a4-9829-2459fd3306d9', 'timestamp': '2017-10-05T19:16:44.113Z', 'lang': 'en',
       'result': {'resolvedQuery': 'hello how are you doing',
                  'fulfillment': {'speech': ''}, 'source': 'agent', 'contexts': [], 'metadata': {}, 'score': 0.0},
       'sessionId': 'd6c71cb6ec1947e28048c1688f075f7b'}


search = data = {
  "id": "357391d8-17df-4931-925b-bce21e858e77",
  "timestamp": "2017-10-09T06:32:17.979Z",
  "lang": "en",
  "result": {
    "source": "agent",
    "resolvedQuery": "google what time to sleep",
    "action": "bot.search",
    "actionIncomplete": False,
    "parameters": {
      "searchterm": "what time to sleep"
    },
    "contexts": [],
    "metadata": {
      "intentId": "94a1948b-9715-4c13-89aa-7a3445b50b79",
      "webhookUsed": "false",
      "webhookForSlotFillingUsed": "false",
      "intentName": "bot.search"
    },
    "fulfillment": {
      "speech": "searching...",
      "messages": [
        {
          "type": 0,
          "id": "9ff1edf1-2438-4d0c-a817-13eb179ae24c",
          "speech": "searching..."
        }
      ]
    },
    "score": 0.8999999761581421
  },
  "status": {
    "code": 200,
    "errorType": "success"
  },
  "sessionId": "b09faa77-94ca-44d6-bc99-0fbed70778f8"
}