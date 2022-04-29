# 1.3 URLify

def urlify(string: str) -> str:
    return string.replace(' ', '%20')

def main():
    string = input('Enter a string with spaces: ')

    print(urlify(string))

if __name__ == '__main__':
    main()
