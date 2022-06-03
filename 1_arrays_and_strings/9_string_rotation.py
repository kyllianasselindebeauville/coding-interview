# 1.9 String Rotation

def is_substring(string: str, substring: str):
    """Checks if a string is a substring of another string.

    Uses the string find() method to check if the substring is in the string.

    Args:
        string: A string.
        substring: A substring to look for.

    Returns:
        A boolean equals to True if the substring is really one, False
        otherwise.
    """
    return string.find(substring) != -1


def is_rotation(string1: str, string2: str):
    """Checks if the second string is a rotation of the first one.

    Checks if the second string is a substring of 2 times the first string to
    determine if it is a rotation or not.

    Args:
        string1: A string.
        string2: Another string.

    Returns:
        A boolean equals to True if the second string is a rotation of the
        first one, False otherwise.
    """
    if len(string1) == len(string2) != 0:
        return is_substring(2 * string1, string2)

    return False


def main():
    string1 = input('Enter a string: ')
    string2 = input('Enter another string: ')

    if (is_rotation(string1, string2)):
        print(f'"{string2}" is a rotation of "{string1}"')
    else:
        print(f'"{string2}" is not a rotation of "{string1}"')


if __name__ == '__main__':
    main()
