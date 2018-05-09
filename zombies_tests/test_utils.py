from flask_ask.models import _Field

from zombies.utils import get_slot
from zombies_tests.factories import get_intent, slot


def test_get_slots(self):
    intent = get_intent('FakeIntent', 'CONFIRMED')
    intent['request']['intent'].update({
        "slots": {
            "fake": slot("fake", "value", "slot_id", confirmed='CONFIRMED'),
        }
    })
    self.app.ask.request = _Field(intent['request'])

    fake_slot = get_slot('fake')

    self.assertEqual(fake_slot, {'raw': 'value', 'value': 'value', 'id': 'slot_id'})