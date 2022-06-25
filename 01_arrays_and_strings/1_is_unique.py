# 1.1 Is Unique

def is_unique(string: str) -> bool:
    """Determines if a string has all unique characters.

    Compares the length of the string and the corresponding set to determine if
    all characters are unique.

    Args:
        string: A string.

    Returns:
        A boolean equal to True if all characters are unique, False otherwise.
    """
    return len(string) == len(set(string))


def is_unique_without_data_structures(string: str) -> bool:
    """Determines if a string has all unique characters.

    Loops through each character of the string and checks if it has already
    been seen using bitwise operations.

    Args:
        string: A string.

    Returns:
        A boolean equal to True if all characters are unique, False otherwise.
    """
    bits = 0

    for char in string:
        shift = ord(char)
        if bits & (1 << shift):
            return False
        bits |= (1 << shift)

    return True


def main():
    string = input('Enter a string: ')

    if is_unique(string):
        print('All characters are unique')
    else:
        print('Not all characters are unique')


if __name__ == '__main__':
    main()
