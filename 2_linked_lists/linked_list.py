# Linked List

class LinkedListNode:
    """The node of a linked list or a doubly linked list.

    https://en.wikipedia.org/wiki/Node_(computer_science)

    Attributes:
        data: Data contained in the node.
        next: Next node.
        prev: Previous node.
    """

    def __init__(self, data, next=None, prev=None):
        """Inits LinkedListNode with data and possibly the next and/or the previous node."""
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)


class LinkedList:
    """The linked list data structure.

    https://en.wikipedia.org/wiki/Linked_list

    Attributes:
        head: First node of the linked list.
        tail: Last node of the linked list.
    """

    def __init__(self, values=None):
        """Inits LinkedList with some values."""
        self.head = None
        self.tail = None
        if values is not None:
            for v in values:
                self.append(v)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __len__(self):
        cnt, current = 0, self.head
        while current:
            cnt += 1
            current = current.next
        return cnt

    def __str__(self):
        return ' -> '.join([str(x) for x in self])

    def __add__(self, other):
        return self.__class__([x.data for x in self] + list(other))

    def __radd__(self, other):
        return self.__class__(list(other) + [x.data for x in self])

    def add(self, value):
        """Inserts an element at the beginning of the linked list."""
        if self.head is None:
            self.head = self.tail = LinkedListNode(value)
        else:
            self.head = LinkedListNode(value, next=self.head)

    def append(self, value):
        """Inserts an element at the end of the linked list."""
        if self.head is None:
            self.head = self.tail = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next

    def input(self, type=str):
        """Prompts the user to insert multiple elements to the linked list."""
        print('Enter the elements of the linked list, then press Enter: ')

        while True:
            try:
                input_ = eval(f'{type.__name__}(input())')
            except:
                break

            if input_ == '':
                break

            self.append(input_)


class DoublyLinkedList(LinkedList):
    """The doubly linked list data structure.

    https://en.wikipedia.org/wiki/Doubly_linked_list

    Attributes:
        head: First node of the doubly linked list.
        tail: Last node of the doubly linked list.
    """

    def __str__(self):
        return ' <-> '.join([str(x) for x in self])

    def add(self, value):
        """Inserts an element at the beginning of the doubly linked list."""
        if self.head is None:
            self.head = self.tail = LinkedListNode(value)
        else:
            self.head.prev = LinkedListNode(value, next=self.head)
            self.head = self.head.prev

    def append(self, value):
        """Inserts an element at the end of the doubly linked list."""
        if self.head is None:
            self.head = self.tail = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value, prev=self.tail)
            self.tail = self.tail.next
