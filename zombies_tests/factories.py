import json
import os

THIS_DIR = os.path.dirname(__file__)


def get_intent(intent_name):
    intent = json.load(open(os.path.join(THIS_DIR, 'alexa-intent-request.json')))
    intent['request']['intent'] = {
        'name': intent_name
    }
    return intent



