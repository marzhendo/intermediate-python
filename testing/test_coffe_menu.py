from coffee_menu import CoffeeMenu
import unittest

class TestCoffeeMenu(unittest.TestCase):
    def setUp(self):
        self.coffee_menu = CoffeeMenu()
    def test_get_price_existing_item(self):
        self.assertEqual(self.coffee_menu.get_price('latte'), 2.75)
    def test_get_price_non_existing_item(self):
        self.assertIsNone(self.coffee_menu.get_price('nasi goreng'))
    def test_add_item(self):
        self.coffee_menu.add_item('mocha', 3.00)
        self.assertEqual(self.coffee_menu.get_price('mocha'), 3.00)
    def test_update_item_price(self):
        self.coffee_menu.add_item('espresso', 2.80)
        self.assertEqual(self.coffee_menu.get_price('espresso'), 2.80)
    def test_menu_integrity(self):
        expected_menu = {
            'espresso': 2.50,
            'latte': 2.75,
            'cappuccino': 3.20,
            'americano': 2.70
        }
        self.assertEqual(self.coffee_menu.menu, expected_menu)
    def test_menu_after_adding_item(self):
        self.coffee_menu.add_item('flat white', 3.10)
        expected_menu = {
            'espresso': 2.50,
            'latte': 2.75,
            'cappuccino': 3.20,
            'americano': 2.70,
            'flat white': 3.10
        }
        self.assertEqual(self.coffee_menu.menu, expected_menu)
    def test_menu_after_updating_item(self):
        self.coffee_menu.add_item('cappuccino', 3.50)
        expected_menu = {
            'espresso': 2.50,
            'latte': 2.75,
            'cappuccino': 3.50,
            'americano': 2.70
        }
        self.assertEqual(self.coffee_menu.menu, expected_menu)
    def test_get_price_case_sensitivity(self):
        self.assertIsNone(self.coffee_menu.get_price('Latte'))
    def test_add_item_case_sensitivity(self):
        self.coffee_menu.add_item('Latte', 3.00)
        self.assertEqual(self.coffee_menu.get_price('Latte'), 3.00)
        self.assertEqual(self.coffee_menu.get_price('latte'), 2.75)
    def test_add_item_negative_price(self):
        self.coffee_menu.add_item('test negative', -1.00)
        self.assertEqual(self.coffee_menu.get_price('test negative'), -1.00)
    def test_add_item_zero_price(self):
        self.coffee_menu.add_item('test zero', 0.00)
        self.assertEqual(self.coffee_menu.get_price('test zero'), 0.00)
    def test_large_price(self):
        self.coffee_menu.add_item('test large', 1e6)
        self.assertEqual(self.coffee_menu.get_price('test large'), 1e6)
    def test_float_precision(self):
        self.coffee_menu.add_item('test float', 2.3333333)
        self.assertAlmostEqual(self.coffee_menu.get_price('test float'), 2.3333333)
    def test_special_characters_in_item(self):
        self.coffee_menu.add_item('café mocha!', 3.50)
        self.assertEqual(self.coffee_menu.get_price('café mocha!'), 3.50)
    def test_whitespace_in_item(self):
        self.coffee_menu.add_item('  iced latte  ', 3.00)
        self.assertEqual(self.coffee_menu.get_price('  iced latte  '), 3.00)
    def test_empty_string_item(self):
        self.coffee_menu.add_item('', 1.00)
        self.assertEqual(self.coffee_menu.get_price(''), 1.00)
    def test_none_item(self):
        self.coffee_menu.add_item(None, 1.50)
        self.assertEqual(self.coffee_menu.get_price(None), 1.50)
    def test_numeric_item_name(self):
        self.coffee_menu.add_item(12345, 2.00)
        self.assertEqual(self.coffee_menu.get_price(12345), 2.00)
    def test_duplicate_item_addition(self):
        self.coffee_menu.add_item('espresso', 2.60)
        self.assertEqual(self.coffee_menu.get_price('espresso'), 2.60)
    def test_multiple_item_additions(self):
        items_to_add = {
            'macchiato': 3.00,
            'ristretto': 2.80,
            'affogato': 4.00
        }
        for item, price in items_to_add.items():
            self.coffee_menu.add_item(item, price)
        for item, price in items_to_add.items():
            self.assertEqual(self.coffee_menu.get_price(item), price)
    def tearDown(self):
        self.coffee_menu = None
if __name__ == '__main__':
    unittest.main()