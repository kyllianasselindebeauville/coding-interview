# 1.2 Check Permutation

def permutation(string1: str, string2: str) -> bool:
    if len(string1) != len(string2):
        return False
    return sorted(string1) == sorted(string2)

def main():
    string1 = input('Enter a string: ')
    string2 = input('Enter another string: ')

    if permutation(string1, string2):
        print('Strings are permutations')
    else:
        print('Strings are not permutations')

if __name__ == '__main__':
    main()
