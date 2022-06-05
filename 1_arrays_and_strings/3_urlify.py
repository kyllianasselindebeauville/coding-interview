# 1.3 URLify

def urlify(string: str) -> str:
    """Replaces spaces of a string with %20 .

    Uses the str strip() and replace() methods to urlify the string.

    Args:
        string: A string.

    Returns:
        A string without spaces but with %20 instead.
    """
    return string.strip().replace(' ', '%20')


def urlify_without_replace(string: str) -> str:
    """Replaces spaces of a string with %20 .

    Uses the str split() and join() methods to urlify the string.
    The result is incorrect if there are several spaces in a row.

    Args:
        string: A string.

    Returns:
        A string without spaces but with %20 instead.
    """
    return '%20'.join(string.split())


def main():
    string = input('Enter a string with spaces: ')

    print(urlify(string))


if __name__ == '__main__':
    main()
