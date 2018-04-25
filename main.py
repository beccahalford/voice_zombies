from flask import Flask
from flask_ask import Ask, statement, request, delegate
from random import *

from facts import random_facts, der_reise, five
from map_selector import select_map_fact

app = Flask(__name__)
ask = Ask(app, '/')


def get_slots():
    ret = {}
    slots = request.intent.slots
    for key in slots.keys():
        for resolution in slots[key].get('resolutions', {}).get('resolutionsPerAuthority', []):
            if resolution['status']['code'] == 'ER_SUCCESS_MATCH':
                ret[key] = resolution['values'][0]
                break

    return ret


@ask.intent('RandomFactIntent')
def get_random_fact():

    fact_no = randint(1, 10)
    fact = random_facts[fact_no]

    speech_text = fact
    return statement(speech_text).simple_card("Zombies Fact", speech_text)


@ask.intent('MapIntent')
def get_map_fact(x):
    slots = get_slots()

    if 'map' not in slots:
        return delegate()

    map = slots['map']
    map_id = map['value']['id']

    # return statement("Map name: {name}, Map ID: {id}".format(name=map['value']['name'], id=map['value']['id']))
    fact = select_map_fact(map_id)

    return statement("No facts available for {}" + format(map))


if __name__ == '__main__':
    app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)

