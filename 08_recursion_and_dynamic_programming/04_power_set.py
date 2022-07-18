# 8.4 Power Set

import unittest


def subsets(set_):
    subsets = list()

    for i in range(1 << len(set_)):
        subset = set(v for k, v in enumerate(set_) if i & (1 << k))
        subsets.append(subset)

    return subsets


class Test(unittest.TestCase):
    def test_subsets(self):
        set_ = set()
        self.assertEqual(len(subsets(set_)), 1)

        set_ = {'a'}
        self.assertEqual(len(subsets(set_)), 2)

        set_ = {'a', 'b'}
        self.assertEqual(len(subsets(set_)), 4)

        set_ = {'a', 'b', 'c'}
        self.assertEqual(len(subsets(set_)), 8)


if __name__ == '__main__':
    unittest.main()
