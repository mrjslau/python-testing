import unittest, doctest
import prime


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(prime))
    return tests

if __name__ == '__main__':
    unittest.main()