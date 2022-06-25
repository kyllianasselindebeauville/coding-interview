# Stack

class Stack:
    def __init__(self, items=None):
        self.items = list()

        if items is not None:
            for i in items:
                self.push(i)

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return ' -> '.join([str(x) for x in self])

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None

        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None

        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def input(self, type=str):
        print(f'Enter the elements ({type.__name__}) of the stack, then press Enter: ')

        while True:
            try:
                input_ = eval(f'{type.__name__}(input())')
            except:
                break

            if input_ == '':
                break

            self.push(input_)
