class reverse_iter:

    def __init__(self, elements):
        self.elements = elements
        self.start = len(self.elements) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 0:
            raise StopIteration
        index = self.start
        self.start -= 1
        return self.elements[index]
