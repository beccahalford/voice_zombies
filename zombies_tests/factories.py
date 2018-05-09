import json
import os

THIS_DIR = os.path.dirname(__file__)


def get_intent(intent_name, confirmation='NONE'):
    intent = json.load(open(os.path.join(THIS_DIR, 'alexa-intent-request.json')))
    intent['request']['intent'] = {
        'name': intent_name,
        'confirmationStatus': confirmation
    }
    return intent


def slot(name, value=None, slot_id=None, confirmed='NONE'):
    slot = {
        "name": name,
        "resolutions": {
            "resolutionsPerAuthority": [
                {
                    "authority": "<authority>",
                    "status": {
                        "code": "ER_NO_MATCH"
                    },
                    "values": []
                }
            ]
        },
        "confirmationStatus": confirmed
    }

    if value:
        slot['value'] = value
        slot['resolutions']['resolutionsPerAuthority'][0]['status']['code'] = 'ER_SUCCESS_MATCH'
        slot['resolutions']['resolutionsPerAuthority'][0]['values'].append({
            "value": {
                "name": value,
                "id": slot_id
            }
        })

    return slot


def map_fact_intent():
    intent = get_intent('MapIntent', 'CONFIRMED')
    intent['request']['intent'].update({
        "slots": {
            "map": slot("map", "Der Riese", "der_riese", confirmed='CONFIRMED'),
        }
    })
    return intent


def perk_location_intent():
    intent = get_intent('PerkLocationIntent', 'CONFIRMED')
    intent['request']['intent'].update({
        "slots": {
            "map": slot("map", "Der Riese", "der_riese", confirmed='CONFIRMED'),
            "perk": slot("perk", "Jugg", "juggernog", confirmed='CONFIRMED'),
        }
    })
    return intent


def gobblegum_intent():
    intent = get_intent('GobbleGumIntent')
    intent['request']['intent'].update({
        "slots": {
            "gobblegum": slot("gobblegum", "Perkaholic", "perkaholic"),
        }
    })
    return intent
