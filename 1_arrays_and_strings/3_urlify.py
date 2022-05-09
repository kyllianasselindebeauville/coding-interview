# 1.3 URLify

def urlify(string: str) -> str:
    """Replaces spaces of a string with %20 .

    Uses the string replace() method to urlify the string.

    Args:
        string: A string.

    Returns:
        A string without spaces but with %20 instead.
    """
    return string.replace(' ', '%20')

def main():
    string = input('Enter a string with spaces: ')

    print(urlify(string))

if __name__ == '__main__':
    main()
