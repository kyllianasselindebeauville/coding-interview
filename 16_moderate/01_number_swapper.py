# 16.1 Number Swapper

import unittest


def swap(a, b):
    a ^= b
    b ^= a
    a ^= b
    return a, b


class Test(unittest.TestCase):
    def test_swap(self):
        a, b = 8, 24
        self.assertEqual(swap(a, b), (b, a))


if __name__ == '__main__':
    unittest.main()
