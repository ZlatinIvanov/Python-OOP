def start_playing(obj):
    return obj.play()


class Guitar:

    def play(self) -> str:
        return "Playing the guitar"


guitar = Guitar()
print(start_playing(guitar))


class Children:

    def play(self) -> str:
        return "Children are playing"


children = Children()
print(start_playing(children))
