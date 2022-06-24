# 2.8 Loop Detection

from linked_list import LinkedList


def loop_detection(ll):
    current = runner = ll.head

    while runner and runner.next:
        current, runner = current.next, runner.next.next

        if current is runner:
            break

    if runner is None or runner.next is None:
        return None

    current = ll.head

    while current is not runner:
        current, runner = current.next, runner.next

    return current


def main():
    ll1, ll2 = LinkedList(), LinkedList()
    ll1.input()
    ll2.input()

    if ll1.head is None:
        ll1.head = ll1.tail = ll2.head
    if ll2.head is not None:
        ll1.tail.next, ll1.tail = ll2.head, ll2.head
        ll1.tail.next, ll1.tail = ll2.head, ll2.head

    print(f'The node at the beginning of the loop is: {loop_detection(ll1)}')


if __name__ == '__main__':
    main()
