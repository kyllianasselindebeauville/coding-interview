# 2.5 Sum Lists

from linked_list import LinkedList


def sum_lists(ll1, ll2):
    result, carry = LinkedList(), 0
    current1, current2 = ll1.head, ll2.head

    while current1 or current2:
        addition = carry

        if current1:
            addition += current1.data
            current1 = current1.next

        if current2:
            addition += current2.data
            current2 = current2.next

        digit = addition % 10
        result.append(digit)

        carry = addition // 10

    if carry != 0:
        result.append(carry)

    return result


def sum_lists_followup(ll1, ll2):
    for _ in range(abs(len(ll1) - len(ll2))):
        (ll1 if len(ll1) < len(ll2) else ll2).add(0)

    result = 0
    current1, current2 = ll1.head, ll2.head

    while current1 and current2:
        result = result * 10 + current1.data + current2.data
        current1, current2 = current1.next, current2.next

    return LinkedList([i for i in str(result)])


def main():
    ll1, ll2 = LinkedList(), LinkedList()
    ll1.input(int)
    ll2.input(int)

    print(ll1, '+', ll2, '=', sum_lists_followup(ll1, ll2), sep='\n')


if __name__ == '__main__':
    main()
