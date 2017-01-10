from wit import Wit
import logging
import json
import os

logger = logging.getLogger(__name__)

access_token = 'A6LUMWS4GCYONHIVTBVSA767AYSXCQUW'

final_response  = {}

def send(request, response):
	fb_id = request['session_id']
	text = response['text']
	global final_response
	final_response = response
	

def first_entity_value(entities, entity):
    """
    Returns first entity value
    """
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val

def get_spotlight(request):

	context = request['context']

	raw_data = os.popen("curl https://vitacademics-rel.herokuapp.com/api/v2/vellore/spotlight").read()
	data = json.loads(raw_data)
	len_acad = len(data['spotlight']['academics'])
	text = '\n'
	for i in range(0,len_acad):
		text = text + data['spotlight']['academics'][i]['text'] + '\n'

	context['spotlight'] = text

	return context

def get_attendance(request):
	context = request['context']
	entities = request['entities']

	subject = first_entity_value(entities,'subject')

	#logger.debug(request)

	if subject:
		context['attendance'] = 10
	else:
		context['attendance'] = 50
	return context


def get_response(received_message,fb_id):
	client.run_actions(session_id = fb_id, message = received_message)
	#TODO: Send request (session id) as well
	return final_response


actions = {
    'send': send,
    'getAttendance': get_attendance,
    'getSpotlight': get_spotlight,
}

client = Wit(access_token=access_token, actions=actions)

