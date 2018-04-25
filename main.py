from flask import Flask
from flask_ask import Ask, statement, request, delegate, question
import random

from facts import random_facts, map_facts, map_information

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

    fact = random.choice(random_facts)
    speech_text = fact
    return statement(speech_text).simple_card("Zombies Fact", speech_text)


@ask.intent('MapIntent')
def get_map_fact(x):
    slots = get_slots()

    if request.get('dialogState', '') != 'COMPLETED':
        return delegate()

    map = slots['map']
    map_id = map['value']['id']

    if map_id not in map_facts:
        return statement("No facts available for {}, map unknown".format(map['value']['name']))

    facts = map_facts[map_id]

    if not len(facts):
        return statement("No facts available for {}".format(map['value']['name']))

    import ipdb
    ipdb.set_trace()
    fact = random.choice(facts)
    return statement(fact)


@ask.intent('PerkLocationIntent')
def get_map_perk_location():
    slots = get_slots()

    if request.get('dialogState', '') != 'COMPLETED':
        return delegate()


    map = slots['map']
    map_id = map['value']['id']

    if map_id == 'nacht':
        return statement('Nacht Der Untoten does not have any perks.')

    if map_id not in map_information:
        return statement("Sorry, I could not find the perk location on {}, map unknown".format(map['value']['name']))

    perk = slots['perk']
    perk_id = perk['value']['id']
    if perk_id not in map_information[map_id]:
        return statement("Sorry, this {} is not available in {} ".format(perk['value']['name'], map['value']['name']))

    perk_location = map_information[map_id][perk_id]

    return statement(perk_location)


if __name__ == '__main__':
    app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)

