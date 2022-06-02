# 1.5 One Away

def one_edit_away(string1: str, string2: str) -> bool:
    """Determines if two strings are one edit away.

    Iterates through the strings and looks for differences to determine if
    the strings are one edit away (insertion of a character, removal of a
    character, replacement of a character).

    Args:
        string1: A string.
        string2: Another string.

    Returns:
        A boolean equal to True if the strings are one edit away, False
        otherwise.
    """
    if abs(len(string1) - len(string2)) > 1:
        return False

    index1, index2, diff = 0, 0, False

    while index1 < len(string1) and index2 < len(string2):
        if string1[index1] != string2[index2]:
            if diff:
                return False
            diff = True
            index1 -= (0, 1)[len(string1) < len(string2)]
            index2 -= (0, 1)[len(string2) < len(string1)]
        index1 += 1
        index2 += 1

    return True


def main():
    string1 = input('Enter a string: ')
    string2 = input('Enter another string: ')

    if one_edit_away(string1, string2):
        print('Strings are one edit away')
    else:
        print('Strings are not one edit away')


if __name__ == '__main__':
    main()
