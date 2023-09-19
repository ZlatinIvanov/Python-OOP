from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):

    def setUp(self) -> None:
        self.car = SecondHandCar("Ford", "Mustang", 1000, 10000)
        self.car2 = SecondHandCar("Opel", "Astra", 5000, 5000)
        self.car3 = SecondHandCar("Ford", "Mustang", 5000, 5000)

    def test_correct_initialization(self):
        self.assertEqual("Ford", self.car.model)
        self.assertEqual("Mustang", self.car.car_type)
        self.assertEqual(1000, self.car.mileage)
        self.assertEqual(10000, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_setter_raise_error(self):

        with self.assertRaises(ValueError) as ve:
            self.car.price = 0

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_mileage_setter_raise_error(self):

        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 0

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_set_promotional_price_new_price_higher_raise_error(self):

        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(20000)

        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotional_price_successfully_changed(self):

        result = self.car.set_promotional_price(5000)

        self.assertEqual(5000, self.car.price)
        self.assertEqual('The promotional price has been successfully set.', result)

    def test_repair_car_successfully_increase_price(self):
        result = self.car.need_repair(1000, "Painting")

        self.assertEqual(11000, self.car.price)
        self.assertEqual(["Painting"], self.car.repairs)
        self.assertEqual('Price has been increased due to repair charges.', result)

    def test_repair_car_not_possible_due_to_high_price_raise_error(self):
        result = self.car.need_repair(10000, "New Engine")

        self.assertEqual('Repair is impossible!', result)

    def test_compare_two_cars_by_price_error_mismatch_car_types_raise_error(self):

        result = self.car.__gt__(self.car2)

        self.assertEqual('Cars cannot be compared. Type mismatch!', result)

    def test_compare_two_cars_by_price_successfully(self):

        result = self.car.__gt__(self.car3)

        self.assertEqual(True, result)

    def test_correct__str__(self):
        result = f"""Model Ford | Type Mustang | Milage 1000km
Current price: 10000.00 | Number of Repairs: 0"""

        self.assertEqual(result, str(self.car))


if __name__ == "__main__":
    main()