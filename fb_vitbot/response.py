from wit import Wit
import logging


logger = logging.getLogger(__name__)

access_token = 'A6LUMWS4GCYONHIVTBVSA767AYSXCQUW'

final_response = None

def send(request, response):
	fb_id = request['session_id']
	text = response['text']
	final_response = response
	print(fb_id,text)


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
}

client = Wit(access_token=access_token, actions=actions)

#get_response('Tell me my attendance in linear algebra','dfaverw23')