import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    def test_numbuses_example_1(self):
        """ Test number of buses with 0 people """

        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_numbuses_example_2(self):
        """ Test number of buses with 25 people """

        actual = a1.num_buses(25)
        expected = 1
        self.assertEqual(actual, expected)

    def test_numbuses_example_3(self):
        """ Test number of buses with 49 people """

        actual = a1.num_buses(49)
        expected = 1
        self.assertEqual(actual, expected)

    def test_numbuses_example_4(self):
        """ Test number of buses with 50 people """

        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(actual, expected)

    def test_numbuses_example_5(self):
        """ Test number of buses with 51 people """

        actual = a1.num_buses(51)
        expected = 2
        self.assertEqual(actual, expected)

    def test_numbuses_example_6(self):
        """ Test number of buses with 75 people """

        actual = a1.num_buses(75)
        expected = 2
        self.assertEqual(actual, expected)

    def test_numbuses_example_7(self):
        """ Test number of buses with 101 people """

        actual = a1.num_buses(101)
        expected = 3
        self.assertEqual(actual, expected)
if __name__ == '__main__':
    unittest.main(exit=False)
