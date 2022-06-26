# 3.4 Queue via Stacks

from stack import Stack
from queue import Queue


class MyQueue:
    def __init__(self, items=None):
        self.add_stack = Stack()
        self.remove_stack = Stack()

        if items is not None:
            for i in items:
                self.add_stack.push(i)

    def __iter__(self):
        return iter(list(self.remove_stack)[::-1] + list(self.add_stack))

    def __len__(self):
        return len([_ for _ in self])

    def __str__(self):
        return ' <- '.join([str(x) for x in self])

    def add(self, item):
        self.add_stack.push(item)

    def remove(self):
        if self.remove_stack.is_empty():
            if self.add_stack.is_empty():
                return None

            while self.add_stack:
                self.remove_stack.push(self.add_stack.pop())

        return self.remove_stack.pop()

    def peek(self):
        if self.remove_stack.is_empty():
            if self.add_stack.is_empty():
                return None

            while self.add_stack:
                self.remove_stack.push(self.add_stack.pop())

        return self.remove_stack.peek()


def main():
    queue = MyQueue(Queue().input())
    print(queue)


if __name__ == '__main__':
    main()
