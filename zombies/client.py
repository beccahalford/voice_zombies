import random
import requests


class Client:

    token = 'aa26cf509cd32f729c00fad75546ab3b8a0381e3'

    def __init__(self):
        self.session = requests.session()
        self.session.headers.update(
            {'Content-type': 'application/json',
             'Authorization': 'Token {}'.format(self.token)}
        )
        self.base_url = 'http://localhost:8000/zombies/api'

    def get_random_fact(self):
        url = '{base_url}/random_fact'.format(base_url=self.base_url)

        facts = self.session.get(url).json()
        fact = random.choice(facts)

        return fact['description']

    def get_map_fact(self, map_id):
        url = '{base_url}/map_fact/?map={map_id}'.format(base_url=self.base_url, map_id=map_id)
        map_facts = self.session.get(url).json()
        if not len(map_facts):
            return ''

        fact = random.choice(map_facts)

        return fact['description']

    def get_perk_location(self, map_id, perk_id):
        url = '{base_url}/map/{map_id}'.format(base_url=self.base_url, map_id=map_id)
        map_perks = self.session.get(url).json()

        if len(map_perks['perks']) == 0:
            return 'no_perk_location'

        try:
            perk = [perk for perk in map_perks['perks'] if perk['perk_id'] == perk_id][0]
        except IndexError:
            perk = None
            return perk

        return perk['location']

    def get_gobblegum(self, gobblegum_id):
        url = '{base_url}/gobblegum/?gobblegum_id={gobblegum_id}'.format(base_url=self.base_url, gobblegum_id=gobblegum_id)
        gobblegum_data = self.session.get(url).json()

        if not len(gobblegum_data):
            return ''

        return gobblegum_data[0]['description']