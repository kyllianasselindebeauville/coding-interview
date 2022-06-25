# 2.1 Remove Dups

from linked_list import LinkedList


def remove_dups(ll):
    """Removes duplicates from a linked list.

    Iterates through the linked list and removes elements that have already
    been seen.

    Args:
        ll: A linked list.

    Returns:
        None.
    """
    seen, previous = set(), None

    for current in ll:
        if current.data not in seen:
            seen.add(current.data)
            previous = current
        else:
            previous.next = current.next


def remove_dups_followup(ll):
    """Removes duplicates from a linked list.

    Iterates through the linked list and uses a second iteration to remove
    elements that are similar to the current one.

    Args:
        ll: A linked list.

    Returns:
        None.
    """
    current, runner = ll.head, None

    while current:
        runner = current

        while runner.next:
            if runner.next.data != current.data:
                runner = runner.next
            else:
                runner.next = runner.next.next

        current = current.next


def main():
    ll = LinkedList()
    ll.input()
    print(ll)

    remove_dups(ll)
    print(ll)


if __name__ == '__main__':
    main()
