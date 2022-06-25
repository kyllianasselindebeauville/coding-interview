# 2.3 Delete Middle Node

from linked_list import LinkedList


def delete_node(node):
    """Deletes a node in the middle of a linked list.

    Assigns the data and the next element of the next node to the current one.

    Args:
        node: A linked list node.

    Returns:
        None.
    """
    if node is not None and node.next is not None:
        node.data, node.next = node.next.data, node.next.next


def main():
    ll = LinkedList().input()
    print(ll)

    index = int(input('Enter the index of the node you want to delete: '))
    if 0 <= index < len(ll):
        node = eval('ll.head' + '.next' * index)
    else:
        node = None

    delete_node(node)
    print(ll)


if __name__ == '__main__':
    main()
