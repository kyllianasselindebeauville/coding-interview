# 3.5 Sort Stack

from stack import Stack


def sort(stack):
    sorted_stack = Stack()

    while stack:
        temp = stack.pop()

        while sorted_stack and temp < sorted_stack.peek():
            stack.push(sorted_stack.pop())

        sorted_stack.push(temp)

    while sorted_stack:
        stack.push(sorted_stack.pop())


def main():
    stack = Stack().input(int)
    print(stack)

    sort(stack)
    print(stack)


if __name__ == '__main__':
    main()
