import unittest
from function import is_a_prime


class FunctionTests(unittest.TestCase):
    def test_prime_factor(self):
        """is_a_prime should return prime factor of a given non prime number"""
        t = 969
        pf = is_a_prime(t)
        self.assertEqual(
                is_a_prime(pf[0]), pf[0]
            )
        self.assertEqual(
                pf[0] * pf[1], t
        )


if __name__ == '__main__':
    unittest.main()
