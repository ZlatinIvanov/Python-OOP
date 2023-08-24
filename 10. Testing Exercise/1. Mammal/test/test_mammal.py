from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal(
            "some name",
            "some type",
            "some sound"
        )

    def test_correct_initialization(self):
        self.assertEqual("some name", self.mammal.name)
        self.assertEqual("some type", self.mammal.type)
        self.assertEqual("some sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_if_make_sound_returns_the_correct_message(self):
        result = self.mammal.make_sound()
        self.assertEqual("some name makes some sound", self.mammal.make_sound())

    def test_if_the_get_kingdom_is_correct(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_if_info_is_correct(self):
        result = self.mammal.info()
        self.assertEqual("some name is of type some type", result)


if __name__ == "__main__":
    main()