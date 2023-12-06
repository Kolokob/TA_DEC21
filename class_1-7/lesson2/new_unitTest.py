import unittest



def calculate_sum(num1, num2):
    return num1 + num2

class MyFirstUnitTest(unittest.TestCase):
    def test_something(self):
        self.assertNotEqual(True, False)  # add assertion here

    def test_add_positive_ints(self):
        self.assertEqual(3, calculate_sum(2, 3))






if __name__ == '__main__':
    unittest.main()
