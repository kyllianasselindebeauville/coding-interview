# 1.1 Is Unique

def is_unique(string: str) -> bool:
    return len(string) == len(set(string))

def is_unique_without_data_structures(string: str) -> bool:
    bits = 0
    for char in string:
        shift = ord(char)
        if bits & (1 << shift):
            return False
        bits |= (1 << shift)
    return True

def main():
    string = input('Enter a string: ')

    if is_unique_without_data_structures(string):
        print('All characters are unique')
    else:
        print('Not all characters are unique')

if __name__ == '__main__':
    main()
