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

# "slots": {
#     "map": {
#         "name": "map",
#         "value": "der Reese",
#         "resolutions": {
#             "resolutionsPerAuthority": [
#                 {
#                     "authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.4b1e2fd2-179f-43e8-9214-bdbc8b3177ab.MAP",
#                     "status": {
#                         "code": "ER_SUCCESS_MATCH"
#                     },
#                     "values": [
#                         {
#                             "value": {
#                                 "name": "Der Riese",
#                                 "id": "der_riese"
#                             }
#                         }
#                     ]
#                 }
#             ]
#         },


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
