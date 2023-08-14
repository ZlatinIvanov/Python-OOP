from project.cat import Cat


class Kitten(Cat):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.gender = "Female"

    def make_sound(self):
        return "Meow"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {__class__.__name__}"