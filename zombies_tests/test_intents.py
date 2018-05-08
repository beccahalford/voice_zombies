import json

from flask import url_for
from flask_testing import TestCase
from zombies.main import app

from zombies_tests.factories import get_intent


class TestIntents(TestCase):
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

    def create_app(self):
        app.config['ASK_VERIFY_REQUESTS'] = False
        return app
