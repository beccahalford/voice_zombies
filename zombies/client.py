import random
import requests

base_url = 'http://localhost:8000'
token = 'aa26cf509cd32f729c00fad75546ab3b8a0381e3'


def get_rnd_fact():
    url = base_url + '/zombies/api/random_fact/'
    response = requests.get(url, headers={
        'Content-type': 'application/json',
        'Authorization': 'Token {}'.format(token)
    })

    facts = response.json()
    fact = random.choice(facts)

    return fact['description']


def get_map_facts(map_id):
    url = base_url + '/zombies/api/map_fact/?map={map_id}'.format(map_id=map_id)
    response = requests.get(url, headers={
        'Content-type': 'application/json',
        'Authorization': 'Token {}'.format(token)
    })

    if not len(response.json()):
        return ''

    map_facts = response.json()
    fact = random.choice(map_facts)

    return fact['description']


def get_perk_location(map_id, perk_id):
    url = base_url + '/zombies/api/perk/?map={map_id}&perk_id={perk_id}'.format(map_id=map_id, perk_id=perk_id)
    response = requests.get(url, headers={
        'Content-type': 'application/json',
        'Authorization': 'Token {}'.format(token)
    })

    if not len(response.json()):
        return ''

    perk_data = response.json()

    return perk_data[0]['location']


def get_gobblegum(gobblegum_id):
    url = base_url + '/zombies/api/gobblegum/?gobblegum_id={gobblegum_id}'.format(gobblegum_id=gobblegum_id)
    response = requests.get(url, headers={
        'Content-type': 'application/json',
        'Authorization': 'Token {}'.format(token)
    })

    if not len(response.json()):
        return ''

    gobblegum_data = response.json()

    return gobblegum_data[0]['description']


def get_map(map_id):
    url = base_url + '/zombies/api/map/?map_id={map_id}'.format(map_id=map_id)
    response = requests.get(url, headers={
        'Content-type': 'application/json',
        'Authorization': 'Token {}'.format(token)
    })

    if not len(response.json()):
        return ''

    map = response.json()

    return map



