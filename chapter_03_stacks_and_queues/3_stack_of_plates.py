# 3.3 Stack of Plates

from stack import Stack


class SetOfStacks:
    def __init__(self, items=None, capacity=5):
        self.stacks = list()
        self.capacity = capacity

        if items is not None:
            for i in items:
                self.push(i)

    def __iter__(self):
        return iter(self.stacks)

    def __len__(self):
        return sum([len(x) for x in self])

    def __str__(self):
        return '\n'.join([str(x) for x in self])

    def push(self, item):
        stack = self.get_last_stack()

        if stack is None or len(stack) >= self.capacity:
            self.stacks.append(Stack([item]))
        else:
            stack.push(item)

    def pop(self):
        stack = self.get_last_stack()

        if stack is None:
            return None

        item = stack.pop()

        if stack.is_empty():
            self.stacks.pop()

        return item

    def pop_at(self, index):
        stack = self.stacks[index] if 0 <= index < len(self.stacks) else None

        if stack is None:
            return None

        item = stack.pop()

        if stack.is_empty():
            self.stacks.pop(index)

        return item

    def is_empty(self):
        return len(self.stacks) == 0

    def get_last_stack(self):
        if self.is_empty():
            return None

        return self.stacks[-1]


def main():
    capacity = int(input('Enter the capacity of a stack: '))
    stack = SetOfStacks(Stack().input(), capacity)

    print(stack)

    index = int(input('Enter the index of the stack from which you want to pop an item: '))
    stack.pop_at(index)

    print(stack)


if __name__ == '__main__':
    main()
