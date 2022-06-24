# 2.6 Palindrome

from linked_list import LinkedList


def palindrome(ll):
    reversed_ll = LinkedList([x.data for x in ll][::-1])

    current1, current2 = ll.head, reversed_ll.head

    while current1 and current2:
        if current1.data != current2.data:
            return False

        current1, current2 = current1.next, current2.next

    return True


def palindrome_with_stack(ll):
    runner, stack = ll.head, list()

    for current in ll:
        if runner and runner.next:
            stack.append(current.data)
            runner = runner.next.next

        elif runner:
            runner = runner.next

        else:
            top = stack.pop()

            if current.data != top:
                return False

    return True


def main():
    ll = LinkedList()
    ll.input()

    if palindrome_with_stack(ll):
        print(f'{ll} is a palindrome')
    else:
        print(f'{ll} is not a palindrome')


if __name__ == '__main__':
    main()
