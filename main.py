from flask import Flask, render_template, url_for
from flask_ask import Ask, statement, request, delegate, question, session, confirm_slot, elicit_slot, confirm_intent
import random

from facts import random_facts, map_facts, map_perk_locations, gobblegum_data

app = Flask(__name__)
ask = Ask(app, '/')


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


@ask.intent('RandomFactIntent')
def get_random_fact():

    fact = random.choice(random_facts)
    speech_text = fact
    return statement(speech_text).simple_card("Zombies Fact", speech_text)


@ask.intent('MapIntent')
def get_map_fact():
    slot = get_slot('map')

    if not slot['id']:
        if not slot['raw']:
            return elicit_slot('map', 'What\'s the map name?')
        return elicit_slot('map', 'Map {} not found, Please try again.'.format(slot['raw']))

    map_id = slot['id']

    if map_id not in map_facts:
        return elicit_slot('map', 'No map entry for {} yet, please try another map'.format(slot['value']))

    facts = map_facts[map_id]
    if not len(facts) or facts == '':
        return elicit_slot('map', 'No facts available for {} yet, please try another map'.format(slot['value']))

    if not intent_confirmed():
        return confirm_intent('Okay, so you would like a fact on {}'.format(slot['value']))

    fact = random.choice(facts)
    return statement(fact)


@ask.intent('PerkLocationIntent')
def get_map_perk_location():
    map = get_slot('map')
    if not map['id']:
        if not map['raw']:
            return elicit_slot('map', 'What\'s the map name?')
        return elicit_slot('map', 'Map {} not found, Please try again.'.format(map['raw']))

    perk = get_slot('perk')
    if not perk['id']:
        if not perk['raw']:
            return elicit_slot('perk', 'What\'s the perk name?')
        return elicit_slot('perk', 'Perk {} not found, Please try again.'.format(perk['raw']))

    map_id = map['id']
    if map_id == 'nacht':
        return statement('Nacht Der Untoten does not have any perks.')
    if map_id not in map_perk_locations:
        return elicit_slot('map', 'No map entries for {} yet, please try another map'.format(map['value']))

    perk_id = perk['id']
    if perk_id not in map_perk_locations[map_id]:
        return statement("Sorry, {} is not available in {} ".format(perk['value'], map['value']))

    map_name = map['value']
    perk_name = perk['value']

    if not intent_confirmed():
        return confirm_intent('You want me to find the location of {} on {}'.format(perk_name, map_name))

    perk_location = map_perk_locations[map_id][perk_id]
    return statement('On {}, {} {}'.format(map_name, perk_name, perk_location))


@ask.intent('GobbleGumIntent')
def get_gobblegum_data():
    slot = get_slot('gobblegum')

    if not slot['id']:
        if not slot['raw']:
            return elicit_slot('gobblegum', 'What\'s the gobble gum name?')
        return elicit_slot('gobblegum', 'Gobble Gum {} not found, Please try again.'.format(slot['raw']))

    gobblegum = slot['value']
    gobblegum_desc = gobblegum_data[slot['id']]['description']
    gobblegum_url = url_for('static', filename='gobblegum/'+slot['id']+'.png', _external=True)

    gobblegum_url = gobblegum_url.replace('http', 'https')

    monty_statement = render_template('gobblegum', gobblegum=gobblegum, gobblegum_desc=gobblegum_desc)
    return statement(monty_statement).standard_card(
        title="Gobblegum",
        text=monty_statement,
        small_image_url=gobblegum_url
    )


@ask.intent('AMAZON.StopIntent')
def stop():
    return statement('OK no problem')


def intent_confirmed():
    return request.intent.confirmationStatus == 'CONFIRMED'


if __name__ == '__main__':
    app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)

