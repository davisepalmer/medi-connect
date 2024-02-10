import unittest
from Supply import * 

#  ^^^ move to src to test then move back to tests or paste path into cli


class TestSupplyMethods(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_decQuantity(self):
        # Test decQuantity method
        supply = Supply(isNeeded=True, item="Test Item", quantity=10, originHosp="Hospital A")
        supply.decQuantity(count=2)
        self.assertEqual(supply.quantity, 8)

    def test_changeOriginHosp(self):
        # Test changeOriginHosp method
        supply = Supply(isNeeded=True, item="Test Item", quantity=10, originHosp="Hospital A")
        supply.changeOriginHosp("Hospital B")
        self.assertEqual(supply.originHosp, "Hospital B")

    def test_changeIsNeeded(self):
        # Test changeIsNeeded method
        supply = Supply(isNeeded=True, item="Test Item", quantity=10, originHosp="Hospital A")
        supply.changeIsNeeded(False)
        self.assertFalse(supply.isNeeded)

    def test_deleteSupple(self):
        # Test deleteSupple method
        supply = Supply(isNeeded=True, item="Test Item", quantity=10, originHosp="Hospital A")
        supply.deleteSupple()
        self.assertFalse(supply.isNeeded)
        self.assertEqual(supply.quantity, -1)
        self.assertEqual(supply.originHosp, "")


if __name__ == '__main__':
    unittest.main()