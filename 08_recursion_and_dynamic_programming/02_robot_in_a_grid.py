# 8.2 Robot in a Grid

import unittest


def find_path_memo(r, c, memo=None):
    if memo is None:
        memo = dict()
    elif (r, c) in memo:
        return memo[(r, c)]

    if r <= 0 or c <= 0:
        return None
    elif r == c == 1:
        return []

    move_right = find_path_memo(r, c - 1, memo)
    move_down = find_path_memo(r - 1, c, memo)

    if move_right is not None:
        memo[(r, c)] = [*move_right, (r, c)]

    elif move_down is not None:
        memo[(r, c)] = [*move_down, (r, c)]

    return memo[(r, c)]


def find_path_tab(r, c):
    if r <= 0 or c <= 0:
        return None

    table = [[[] for _ in range(c + 1)] for _ in range(r + 1)]

    for i in range(len(table)):
        for j in range(len(table[i])):
            if i - 1 > 0:
                table[i][j] = [*table[i - 1][j], (i, j)]
            elif j - 1 > 0:
                table[i][j] = [*table[i][j - 1], (i, j)]

    return table[r][c]


class Test(unittest.TestCase):
    def test_find_path_memo(self):
        self.assertEqual(len(find_path_memo(3, 3)), 4)
        self.assertEqual(find_path_memo(3, 3)[-1], (3, 3))

    def test_find_path_tab(self):
        self.assertEqual(len(find_path_tab(3, 3)), 4)
        self.assertEqual(find_path_tab(3, 3)[-1], (3, 3))


if __name__ == '__main__':
    unittest.main()
