from wit import Wit
import logging


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
	if 'text' not in final_response:
                final_response['text']='I got nothing'
	#TODO: create separate function
	#TODO: Send request (session id) as well
	return final_response


actions = {
    'send': send,
    'getAttendance': get_attendance,
}

client = Wit(access_token=access_token, actions=actions)

