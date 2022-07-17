# 8.1 Triple Step

import unittest


def count_ways_memo(n, memo=None):
    if memo is None:
        memo = dict()
    elif n in memo:
        return memo[n]

    if n == 0:
        return 1
    elif n < 0:
        return 0

    memo[n] = count_ways_memo(n - 1, memo) + count_ways_memo(n - 2, memo) + count_ways_memo(n - 3, memo)
    return memo[n]


def count_ways_tab(n):
    if n < 0:
        return 0

    table = [0 for _ in range(max(3, n + 1))]
    table[0], table[1], table[2] = 1, 1, 2

    for i in range(3, len(table)):
        table[i] = table[i - 1] + table[i - 2] + table[i - 3]

    return table[n]


class Test(unittest.TestCase):
    def test_count_ways_memo(self):
        self.assertEqual(count_ways_memo(1), 1)
        self.assertEqual(count_ways_memo(5), 13)
        self.assertEqual(count_ways_memo(10), 274)

    def test_count_ways_tab(self):
        self.assertEqual(count_ways_tab(1), 1)
        self.assertEqual(count_ways_tab(5), 13)
        self.assertEqual(count_ways_tab(10), 274)


if __name__ == '__main__':
    unittest.main()
