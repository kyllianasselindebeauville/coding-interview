# 1.6 String Compression

def compress(string: str) -> str:
    """Compress a string using run-length encoding.

    Loops over each character in the string and counts the number of
    consecutive occurrences to compress the string.

    Args:
        string: A string.

    Returns:
        A string representing the input string or the input string if the
        compression is useless.
    """
    if not string.isalpha():
        return string

    count, compressed = 0, list()

    for index in range(len(string)):
        count += 1
        if index + 1 >= len(string) or string[index] != string[index + 1]:
            compressed.append(f'{string[index]}{count}')
            count = 0

    compressed_string = ''.join(compressed)
    return (string, compressed_string)[len(compressed_string) <= len(string)]


def main():
    string = input('Enter a string: ')

    print(compress(string))


if __name__ == '__main__':
    main()
