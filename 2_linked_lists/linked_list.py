# Linked List

class LinkedListNode:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, values=None):
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

    def add(self, value):
        if self.head is None:
            self.head = self.tail = LinkedListNode(value)
        else:
            self.head = LinkedListNode(value, next=self.head)

    def append(self, value):
        if self.head is None:
            self.head = self.tail = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next


class DoublyLinkedList(LinkedList):
    def __str__(self):
        return ' <-> '.join([str(x) for x in self])

    def add(self, value):
        if self.head is None:
            self.head = self.tail = LinkedListNode(value)
        else:
            self.head.prev = LinkedListNode(value, next=self.head)
            self.head = self.head.prev

    def append(self, value):
        if self.head is None:
            self.head = self.tail = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value, prev=self.tail)
            self.tail = self.tail.next
