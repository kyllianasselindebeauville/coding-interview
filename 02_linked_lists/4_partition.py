# 2.4 Partition

from linked_list import LinkedList


def partition(ll, x):
    current = ll.tail = ll.head

    while current:
        next_node = current.next

        if current.data < x:
            current.next, ll.head = ll.head, current
        else:
            ll.tail.next, ll.tail = current, current

        current = next_node

    ll.tail.next = None


def main():
    ll = LinkedList().input(int)
    print(ll)

    x = int(input('Enter the value of X: '))
    partition(ll, x)
    print(ll)


if __name__ == '__main__':
    main()
