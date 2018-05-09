from flask_ask.models import _Field
from flask_testing import TestCase

from zombies.main import app
from zombies.utils import get_slot
from zombies_tests.factories import get_intent, slot


class TestUtils(TestCase):
    def create_app(self):
        app.config['ASK_VERIFY_REQUESTS'] = False
        return app

    def test_get_slot(self):
        intent = get_intent('FakeIntent', 'CONFIRMED')
        intent['request']['intent'].update({
            "slots": {
                "fake": slot("fake", "value", "slot_id", confirmed='CONFIRMED'),
            }
        })
        self.app.ask.request = _Field(intent['request'])

        fake_slot = get_slot('fake')

        self.assertEqual(fake_slot, {'raw': 'value', 'value': 'value', 'id': 'slot_id'})
