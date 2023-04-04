import unittest
from utils.arrs import get, my_slice


class TestArrayFunctions(unittest.TestCase):
    def test_get(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(get(arr, 0), None)
        self.assertEqual(get(arr, 3), 4)
        self.assertEqual(get(arr, 6, None), None)
        self.assertEqual(get(arr, -1, None), None)
        self.assertEqual(get(arr, -1, 'default'), 'default')

    def test_my_slice(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(my_slice(arr), [1, 2, 3, 4, 5])
        self.assertEqual(my_slice(arr, 1), [2, 3, 4, 5])
        self.assertEqual(my_slice(arr, 1, 4), [2, 3, 4])
        self.assertEqual(my_slice(arr, 0, 0), [])
        self.assertEqual(my_slice(arr, -1), [5])



if __name__ == '__main__':
    unittest.main()
