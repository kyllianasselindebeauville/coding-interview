# 2.2 Return Kth to Last

from linked_list import LinkedList


def kth_to_last(ll, k):
    """Finds the kth to last element of a linked list.

    Iterates through the linked list using two iterators separated by a
    distance k to find the kth to last element.

    Args:
        ll: A linked list.
        k: An integer representing the K in "Kth to last element".

    Returns:
        The Kth to last element if it exists, None otherwise.
    """
    current = runner = ll.head

    for _ in range(k):
        if runner:
            runner = runner.next
        else:
            return None

    while runner:
        current, runner = current.next, runner.next

    return current


def kth_to_last_with_len(ll, k):
    """Finds the kth to last element of a linked list.

    Iterates through the linked list to find the element at the searched index.

    Args:
        ll: A linked list.
        k: An integer representing the K in "Kth to last element".

    Returns:
        The Kth to last element if it exists, None otherwise.
    """
    length = len(ll)

    if 0 < k <= length:
        for index, current in enumerate(ll):
            if index == length - k:
                return current


def main():
    ll = LinkedList()
    ll.input()
    print(ll)

    k = int(input('Enter the value of K: '))
    print(f'The {k}th to last element is {kth_to_last(ll, k)}')


if __name__ == '__main__':
    main()
