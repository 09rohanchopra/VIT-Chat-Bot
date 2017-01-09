from wit import Wit
import logging

logger = logging.getLogger(__name__)

access_token = 'A6LUMWS4GCYONHIVTBVSA767AYSXCQUW'

def send(request, response):
    print('Sending to user...', response['text'])
def my_action(request):
    print('Received from user...', request['text'])

actions = {
    'send': send,
    'my_action': my_action,
}

client = Wit(access_token=access_token, actions=actions)
resp = client.message('Tell me my attendance in Hindi')
print('Yay, got Wit.ai response: ' + str(resp))
