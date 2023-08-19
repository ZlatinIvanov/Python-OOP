class Stack:

    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        self.data.pop(-1)

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if self.data:
            return False
        return True

    def __str__(self):
        reversed_list = reversed(self.data)
        result = ', '.join(x for x in reversed_list)
        return result
