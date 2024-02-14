""" Pojo Unit Test"""
import unittest

from custom_components.ectocontrol.core.model import EctoControlAPIDevice


class MyTestCase(unittest.TestCase):
    """ Pojo Unit Test Cass"""

    def test_device_init(self):
        """ Test Device Pojo construction from Json dict"""
        data = {
            "id": 1,
            "system_object_id": 1,
            "name": "xx",
            "type": "xx"
        }
        device: EctoControlAPIDevice = EctoControlAPIDevice(**data)
        self.assertEqual(1, device.id)

    def test_device_name(self):
        """ Test Device Pojo post construction name trim"""
        data = {
            "id": 1,
            "system_object_id": 1,
            "name": "xx",
            "type": "xx"
        }
        device: EctoControlAPIDevice = EctoControlAPIDevice(**data)
        self.assertEqual("xx", device.name)
        data = {
            "id": 1,
            "system_object_id": 1,
            "name": "\"xx\"",
            "type": "xx"
        }
        device: EctoControlAPIDevice = EctoControlAPIDevice(**data)
        self.assertEqual("xx", device.name)


if __name__ == '__main__':
    unittest.main()
