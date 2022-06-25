# Queue

class Queue:
    def __init__(self, items=None):
        self.items = list()

        if items is not None:
            for i in items:
                self.add(i)

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return ' <- '.join([str(x) for x in self])

    def add(self, item):
        self.items.append(item)

    def remove(self):
        if self.is_empty():
            return None

        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None

        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0
