from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero("Hero", 1, 100, 100)
        self.enemy = Hero("Enemy", 1, 50, 50)

    def test_correct_initialization(self):
        self.assertEqual("Hero", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_if_enemy_name_is_same_as_hero_raise_exception(self):

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_if_hero_health_is_less_or_equal_to_zero_raise_exception(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        expected = "Your health is lower than or equal to 0. You need to rest"
        self.assertEqual(expected, str(ve.exception))

    def test_if_enemy_health_is_less_or_equal_to_zero_raise_exception(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        expected = f"You cannot fight {self.enemy.username}. He needs to rest"
        self.assertEqual(expected, str(ve.exception))

    def test_battle_enemy_remove_health_after_draw(self):

        self.hero.health = 50

        result = self.hero.battle(self.enemy)
        self.assertEqual(0, self.hero.health)
        self.assertEqual(-50, self.enemy.health)
        self.assertEqual("Draw", result)

    def test_battle_enemy_and_win_expect_stats_improve(self):

        result = self.hero.battle(self.enemy)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(-50, self.enemy.health)
        self.assertEqual(105, self.hero.damage)
        self.assertEqual(2, self.hero.level)
        self.assertEqual("You win", result)

    def test_battle_enemy_and_lose_expect_stats_improve_for_enemy(self):
        self.hero.damage = 10
        self.hero.health = 10
        result = self.hero.battle(self.enemy)
        self.assertEqual(-40, self.hero.health)
        self.assertEqual(45, self.enemy.health)
        self.assertEqual(55, self.enemy.damage)
        self.assertEqual(2, self.enemy.level)
        self.assertEqual("You lose", result)

    def test_correct__str__(self):
        expected = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"
        self.assertEqual(expected, str(self.hero))


if __name__ == "__main__":
    main()
