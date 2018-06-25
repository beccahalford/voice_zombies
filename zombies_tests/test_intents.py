import json

from flask import url_for
from flask_testing import TestCase

from zombies.main import app
from zombies_tests.factories import get_intent, map_fact_intent, gobblegum_intent, perk_location_intent


class TestIntents(TestCase):
    def create_app(self):
        app.config['ASK_VERIFY_REQUESTS'] = False
        return app

    def test_get_random_fact(self):
        data = get_intent('RandomFactIntent')
        response = self.client.post(
            url_for('_flask_view_func'),
            content_type='application/json; charset=utf-8',
            headers={'Signaturecertchainurl': '<cert_chain>', 'Signature': '<signature>'},
            data=json.dumps(data)
        )

        response_data = response.json.get('response', {})
        self.assert200(response)
        self.assertIn('outputSpeech', response_data)
        self.assertEqual(response_data['card']['title'], 'Random Zombies Fact')

    def test_get_map_fact(self):
        data = map_fact_intent()
        response = self.client.post(
            url_for('_flask_view_func'),
            content_type='application/json; charset=utf-8',
            headers={'Signaturecertchainurl': '<cert_chain>', 'Signature': '<signature>'},
            data=json.dumps(data)
        )
        response_data = response.json.get('response', {})
        self.assert200(response)
        self.assertIn('outputSpeech', response_data)

    def test_get_map_perk_location(self):
        data = perk_location_intent()
        response = self.client.post(
            url_for('_flask_view_func'),
            content_type='application/json; charset=utf-8',
            headers={'Signaturecertchainurl': '<cert_chain>', 'Signature': '<signature>'},
            data=json.dumps(data)
        )
        response_data = response.json.get('response', {})
        self.assert200(response)
        self.assertIn('outputSpeech', response_data)

    def test_get_gobblegum_data(self):
        data = gobblegum_intent()
        response = self.client.post(
            url_for('_flask_view_func'),
            content_type='application/json; charset=utf-8',
            headers={'Signaturecertchainurl': '<cert_chain>', 'Signature': '<signature>'},
            data=json.dumps(data)
        )
        response_data = response.json.get('response', {})
        self.assert200(response)
        self.assertIn('outputSpeech', response_data)
        self.assertEqual(response_data['card']['title'], 'Gobblegum')
        self.assertEqual(response_data['card']['text'], 'Perkaholic, ' + 'Gives the player all Perk-a-Colas in the map. 1 activation')