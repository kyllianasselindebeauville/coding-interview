# 8.3 Magic Index

import unittest


def magic_index(arr, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1

    if left > right:
        return None

    mid = (left + right) // 2

    if arr[mid] == mid:
        return mid
    elif arr[mid] < mid:
        return magic_index(arr, mid + 1, right)
    elif arr[mid] > mid:
        return magic_index(arr, left, mid - 1)


def magic_index_followup(arr, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1

    if left > right:
        return None

    mid = (left + right) // 2

    if arr[mid] == mid:
        return mid

    left_search = magic_index_followup(arr, left, min(mid - 1, arr[mid]))
    if left_search is not None:
        return left_search

    right_search = magic_index_followup(arr, max(mid + 1, arr[mid]), right)
    if right_search is not None:
        return right_search


class Test(unittest.TestCase):
    def test_magic_index(self):
        arr = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
        self.assertEqual(magic_index(arr), 7)

    def test_magic_index_followup(self):
        arr = [-10, -5, 2, 2, 2, 3, 4, 5, 9, 12, 13]
        self.assertEqual(magic_index_followup(arr), 2)


if __name__ == '__main__':
    unittest.main()
