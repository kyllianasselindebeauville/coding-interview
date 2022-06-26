# 2.7 Intersection

from linked_list import LinkedList


def intersection(ll1, ll2):
    if ll1.tail is not ll2.tail:
        return None

    current1, current2 = ll1.head, ll2.head

    for _ in range(abs(len(ll1) - len(ll2))):
        if len(ll1) > len(ll2):
            current1 = current1.next
        else:
            current2 = current2.next

    while current1 is not current2:
        current1, current2 = current1.next, current2.next

    return current1


def main():
    ll1, ll2, ll3 = LinkedList().input(), LinkedList().input(), LinkedList().input()

    if ll1.tail is not None:
        ll1.tail.next, ll1.tail = ll3.head, ll3.head
    if ll2.tail is not None:
        ll2.tail.next, ll2.tail = ll3.head, ll3.head

    print(ll1)
    print(ll2)
    print(f'The intersecting node is: {intersection(ll1, ll2)}')


if __name__ == '__main__':
    main()
