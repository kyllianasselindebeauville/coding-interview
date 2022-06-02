# 1.4 Palindrome Permutation

def is_permutation_of_palindrome(string: str) -> bool:
    """Determines if a string is a permutation of a palindrome.

    Counts the number of occurences of each character to determine if the
    string is a permutation of a palindrome.

    Args:
        string: A string.

    Returns:
        A boolean equal to True if the string is a permutation of a palindrome,
        False otherwise.
    """
    chars = dict()

    for c in string.lower():
        chars[c] = chars.get(c, 0) + 1

    odd_chars = dict(filter(lambda x: x[0].isalpha() and x[1] & 1, chars.items()))
    return len(odd_chars) <= 1


def main():
    string = input('Enter a string: ')

    if is_permutation_of_palindrome(string):
        print('Permutation of a palindrome')
    else:
        print('Not a permutation of a palindrome')


if __name__ == '__main__':
    main()
