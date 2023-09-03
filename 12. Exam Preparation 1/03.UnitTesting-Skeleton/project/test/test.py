from unittest import TestCase, main
from project.movie import Movie

class TestMovie(TestCase):

    def setUp(self) -> None:
        self.movie = Movie("Movie", 2000, 10)

    def test_correct_initialization(self):
        self.movie.actors = []
        self.assertEqual(self.movie.name, "Movie")
        self.assertEqual(self.movie.year, 2000)
        self.assertEqual(self.movie.rating, 10)
        self.assertEqual(self.movie.actors, [])

    def test_set_empty_name(self):

        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''

        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_set_incorrect_year(self):

        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1000

        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_new_actor_successfully(self):
        self.assertEqual([], self.movie.actors)
        self.movie.add_actor("Actor2")
        self.assertEqual(["Actor2"], self.movie.actors)

    def test_add_existing_actor_unsuccessful(self):

        self.movie.add_actor("Actor")
        result = self.movie.add_actor("Actor")

        self.assertEqual("Actor is already added in the list of actors!", result)

    def test_if_first_movie_is_gt_second(self):

        movie2 = Movie("Movie2", 2000, 9)

        result = self.movie > movie2

        self.assertEqual(f'"Movie" is better than "Movie2"', result)

    def test_if_second_movie_is_gt_first(self):

        movie2 = Movie("Movie2", 2000, 9)

        result = movie2 > self.movie

        self.assertEqual(f'"Movie" is better than "Movie2"', result)

    def test_if__repr__is_correct(self):

        self.movie.add_actor("Actor")
        self.movie.add_actor("Actor2")

        expected = f"Name: Movie\n" \
               f"Year of Release: 2000\n" \
               f"Rating: 10.00\n" \
               f"Cast: Actor, Actor2"
        result = self.movie.__repr__()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()