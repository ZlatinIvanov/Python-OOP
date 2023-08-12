class Glass:

    CAPACITY = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml):
        if self.content + ml <= Glass.CAPACITY:
            self.content += ml
            return f"Glass filled with {ml} ml"
        return f"Cannot add {ml} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        result = Glass.CAPACITY - self.content
        return f"{result} ml left"

glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())