import unittest
import calculator

class TestCalculator(unittest.TestCase):

    # setUpClass is a one-time set up method that runs once before all the tests run.
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    # tearDownClass is a one-time tear down method that runs once after all the tests are complete.
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    # setUp is a method that runs before every test method.
    def setUp(self):
        print('setup')

    # tearDown is a method that runs after every test method.
    def tearDown(self):
        print('teardown')

    def test_add(self):
        print('testAdd')
        result = calculator.add(5,4)
        self.assertEqual(9, result)

    def test_subtract(self):
        print('testSubtract')
        result = calculator.subtract(6,3)
        self.assertEqual(3, result)

    def test_multiply(self):
        print('testMultiply')
        result = calculator.multiply(3,7)
        self.assertEqual(result, 21)

    def test_divide(self):
        print('testDivide')
        result = calculator.divide(90,5)
        self.assertEqual(result, 18)
        self.assertRaises(ValueError, calculator.divide, 10, 0)

# The following block is the same as python -m unittest test_calculator.py
if __name__ == '__main__':
    unittest.main()