import unittest
from prime import is_a_prime
from conversion import converter


class FunctionTests(unittest.TestCase):
    """
    def test_prime_factor(self):
        "is_a_prime should return prime factor of a given non prime number"
        t = 969
        pf = is_a_prime(t)
        self.assertEqual(
                is_a_prime(pf[0]), pf[0]
            )
        self.assertEqual(
                pf[0] * pf[1], t
        )
    """
    
    def test_convert_fahrenheit(self):
        """converter should return Fahrenheit converted to Celsius and Kelvin"""
        test = 96.8
        self.assertEqual(
                converter(test, 'f', 'c'), 36
        )
        self.assertEqual(
                converter(test, 'f', 'k'), 309.15
        )
    
    def test_convert_celsius(self):
        """converter should return Celsius converted to Fahrenheit and Kelvin"""
        test = 40
        self.assertEqual(
                converter(test, 'c', 'f'), 104
        )
        self.assertEqual(
                converter(test, 'c', 'k'), 313.15
        )

    def test_convert_kelvin(self):
        """converter should return Kelvin converted to Fahrenheit and Celsius"""
        test = 0
        self.assertEqual(
                converter(test, 'k', 'c'), -273.15
        )
        self.assertEqual(
                converter(test, 'k', 'f'), -459.67
        )

    def test_convert_allowed_units(self):
        """converter should only allow F, C and K units"""
        with self.assertRaises(ValueError) as context:
            converter(12, 'a', 'f')

        self.assertTrue("units are invalid. Allowed units ('C', 'F', 'K')" in str(context.exception))

    def test_convert_absolute_zero(self):
        """converter shouldn't allow value less than 0K in any units"""
        self.assertRaises(ValueError, converter, -10, 'k', 'c')
        self.assertRaises(ValueError, converter, -300, 'c', 'f')
        self.assertRaises(ValueError, converter, -459.99, 'f', 'c')

    def test_converter_no_convertion(self):
        """converter should return value even if units are the same"""
        self.assertEqual(converter(12.5, 'c', 'c'), 12.5)

if __name__ == '__main__':
    unittest.main()
