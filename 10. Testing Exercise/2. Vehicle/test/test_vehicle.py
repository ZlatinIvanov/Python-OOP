from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(20.5, 175.5)

    def test_default_consuption_class_attribute_is_correct(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_correct_initialization(self):
        self.assertEqual(20.5, self.vehicle.fuel)
        self.assertEqual(175.5, self.vehicle.horse_power)
        self.assertEqual(20.5, self.vehicle.capacity)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_without_enough_fuel_raises_exception(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_enough_fuel_expect_fuel_decrease(self):
        self.vehicle.drive(2)
        self.assertEqual(18, self.vehicle.fuel)

    def test_refuel_full_car_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_empty_tank_adds_fuel(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(20.5)
        self.assertEqual(20.5, self.vehicle.fuel)

    def test_vehicle__str__return(self):
        result = str(self.vehicle)
        expected = f"The vehicle has {self.vehicle.horse_power} " \
                   f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    main()
