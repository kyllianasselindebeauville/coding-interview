# 8.5 Recursive Multiply

import unittest


def multiply(a, b):
    if a > b:
        a, b = b, a

    if a == 0:
        return 0
    elif a == 1:
        return b

    half = multiply(a >> 1, b)

    if a % 2 == 0:
        return half + half
    else:
        return half + half + b


class Test(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(8, 7), 56)
        self.assertEqual(multiply(17, 23), 391)
        self.assertEqual(multiply(31, 35), 1085)


if __name__ == '__main__':
    unittest.main()
