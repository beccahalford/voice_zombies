from flask_ask import request


def get_slots():
    """
    Get all of our slots out, e.g
        {
            "slot_name": {
                "raw": "Raw Value",
                "matches": [
                    {"value": "value", "id": "slot_id"}
                ],
                "status": "CONFIRMED"
            }
        }
    """
    slots = {}
    # Dig through each slot
    for name, slot in request.intent.slots.items():
        slots[name] = {"raw": slot.get('value'), "matches": [], "status": slot.get('confirmationStatus')}
        # For custom slots, get our successful resolutions
        for resolution in slot.get('resolutions', {}).get('resolutionsPerAuthority', []):
            if resolution['status']['code'] == 'ER_SUCCESS_MATCH':
                for match in resolution['values']:
                    slots[name]['matches'].append({'value': match['value'].get('name'), 'id': match['value'].get('id')})
    return slots


def get_slot(slot_name):
    slots = get_slots()
    matches = slots.get(slot_name, {}).get('matches', [])
    return {
        'raw': slots.get(slot_name, {}).get('raw', None),
        'value': matches[0]['value'] if len(matches) else None,
        'id': matches[0].get('id') if len(matches) else None
    }


def fill_slot(slot_name, slot_value):
    request.intent.slots[slot_name]['value'] = slot_value
    return request
