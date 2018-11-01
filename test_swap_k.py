import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_swapk_1(self):
        """ test with even list and even k"""
        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 2)
        actual = nums
        expected = [5, 6, 3, 4, 1, 2]
        self.assertEqual(actual, expected)
        
    def test_swapk_2(self):
        """ test with k = 0 """
        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 0)
        actual = nums
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(actual, expected)
        
    def test_swapk_3(self):    
        """ test with empty list """
        nums = []
        a1.swap_k(nums, 1)
        actual = nums
        expected = []
        self.assertEqual(actual, expected)
        
    def test_swapk_4(self):
        """ test with list of size 1"""
        nums = [10]
        a1.swap_k(nums, 0)
        actual = nums
        expected = [10]
        self.assertEqual(actual, expected)
        
    def test_swapk_5(self):
        """ test with odd list and odd k """
        nums = [1, 2, 3, 4, 5, 6, 7]
        a1.swap_k(nums, 3)
        actual = nums
        expected = [5, 6, 7, 4, 1, 2, 3]
        self.assertEqual(actual, expected)

    def test_swapk_6(self):
        """ test with odd list and even k """
        nums = [9, 8, 7, 6, 5, 4, 3]
        a1.swap_k(nums, 3)
        actual = nums
        expected = [5, 4, 3, 6, 9, 8, 7]
        self.assertEqual(actual, expected)
        
if __name__ == '__main__':
    unittest.main(exit=False)
