import random

from flask import Flask, render_template, url_for
from flask_ask import Ask, statement, request, elicit_slot, confirm_intent
from zombies.client import Client
from zombies.utils import get_slot

app = Flask(__name__)
ask = Ask(app, '/')
client = Client()


@ask.intent('RandomFactIntent')
def get_random_fact():

    fact = client.get_random_fact()
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

    fact = client.get_map_fact(map_id)

    if not len(fact) or fact == '':
        return elicit_slot('map', render_template('no_map_facts', map=map_name))

    if not intent_confirmed():
        return confirm_intent(render_template('map_confirmation', map=map_name))

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
        return elicit_slot('perk', render_template('perk_unknown', user_value=perk['raw']))

    map_id = map['id']
    map_name = map['value']
    perk_id = perk['id']
    perk_name = perk['value']

    if map_id == 'nacht':
        return statement('Nacht Der Untoten does not have any perks.')

    if not intent_confirmed():
        return confirm_intent(render_template('perk_location_confirmation', map=map_name, perk=perk_name))

    perk_location = client.get_perk_location(map_id, perk_id)

    if perk_location is None:
        return statement(render_template('perk_unavailble', map=map_name, perk=perk_name))

    if perk_location == 'no_perk_location':
        return statement(render_template('no_perk_location', map=map_name, perk=perk_name))

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

    gobblegum_id = slot['id']
    gobblegum = slot['value']
    gobblegum_desc = client.get_gobblegum(gobblegum_id)

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

