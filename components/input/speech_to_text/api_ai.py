import os.path
import sys

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = '4056d8f63dce40a18f26d9689c3a7e98 '


def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.event_request(apiai.events.Event("my_custom_event"))

    request.lang = 'en'  # optional, default value equal 'en'

    request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

    response = request.getresponse()

    print (response.read())


if __name__ == '__main__':
    main()
