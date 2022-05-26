import unittest
from utils import charge
import json

with open("rides.json") as f:
    data = json.load(f)


class TestChargeFunction(unittest.TestCase):
    def test(self):
        self.assertEqual(charge(data[0]), 6)

    def test_night(self):
        self.assertEqual(charge(data[4]), 14)

    def test_busy(self):
        self.assertEqual(charge(data[5]), 14.5)


if __name__ == "__main__":
    unittest.main()
