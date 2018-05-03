from flask import Flask, render_template, url_for
from flask_ask import Ask, statement, request, delegate, question, session, confirm_slot, elicit_slot, confirm_intent
import random

from facts import random_facts, map_facts, map_perk_locations, gobblegum_data
from utils import get_slot

app = Flask(__name__)
ask = Ask(app, '/')


@ask.intent('RandomFactIntent')
def get_random_fact():

    fact = random.choice(random_facts)
    speech_text = fact
    return statement(speech_text).simple_card("Random Zombies Fact", speech_text)


@ask.intent('MapIntent')
def get_map_fact():
    slot = get_slot('map')

    if not slot['id']:
        if not slot['raw']:
            return elicit_slot('map', 'What\'s the map name?')
        return elicit_slot('map', render_template('map_unknown', user_value=slot['raw']))

    map_id = slot['id']
    map_name = slot['value']

    if map_id not in map_facts:
        return elicit_slot('map', render_template('no_map_entry', map=map_name))

    facts = map_facts[map_id]
    if not len(facts) or facts == '':
        return elicit_slot('map', render_template('no_map_entry', map=map_name))

    if not intent_confirmed():
        return confirm_intent(render_template('map_confirmation', map=map_name))

    fact = random.choice(facts)
    return statement(fact)


@ask.intent('PerkLocationIntent')
def get_map_perk_location():
    map = get_slot('map')
    if not map['id']:
        if not map['raw']:
            return elicit_slot('map', 'What\'s the map name?')
        return elicit_slot('map', render_template('map_unknown', user_value=map['raw']))

    perk = get_slot('perk')
    if not perk['id']:
        if not perk['raw']:
            return elicit_slot('perk', 'What\'s the perk name?')
        return elicit_slot('perk', render_template('map_unknown', user_value=perk['raw']))

    map_id = map['id']
    map_name = map['value']
    perk_name = perk['value']

    if map_id == 'nacht':
        return statement('Nacht Der Untoten does not have any perks.')
    if map_id not in map_perk_locations:
        return elicit_slot('map', render_template('no_perk_location', map=map_name))

    perk_id = perk['id']

    if perk_id not in map_perk_locations[map_id]:
        return statement(render_template('perk_location_confirmation', map=map_name, perk=perk_name))

    if not intent_confirmed():
        return confirm_intent(render_template('perk_location_confirmation', map=map_name, perk=perk_name))

    perk_location = map_perk_locations[map_id][perk_id]
    return statement(render_template('perk_location',
                                     map=map_name,
                                     perk=perk_name,
                                     perk_location=perk_location))


@ask.intent('GobbleGumIntent')
def get_gobblegum_data():
    slot = get_slot('gobblegum')

    if not slot['id']:
        if not slot['raw']:
            return elicit_slot('gobblegum', 'What\'s the gobble gum name?')
        return elicit_slot('gobblegum', render_template('gobblegum_unknown', user_value=slot['raw']))

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
    stop_message=random.choice([
        'OK no problem', 'Goodbye', 'Bye for now', 'Speak to you later', 'Until next time', 'bye', 'bye bye',
    ])

    return statement(stop_message)


def intent_confirmed():
    return request.intent.confirmationStatus == 'CONFIRMED'


if __name__ == '__main__':
    app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)

