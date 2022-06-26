# 3.2 Stack Min

from stack import Stack


class StackMin(Stack):
    def __init__(self, items=None):
        self.min_items = Stack()
        super().__init__(items)

    def push(self, item):
        if self.is_empty() or item <= self.min():
            self.min_items.push(item)

        super().push(item)

    def pop(self):
        if self.peek() == self.min():
            self.min_items.pop()

        return super().pop()

    def min(self):
        if self.min_items.is_empty():
            return None

        return self.min_items.peek()


def main():
    stack = StackMin().input(int)
    print(stack)
    print(f'The minimum is: {stack.min()}')


if __name__ == '__main__':
    main()
