from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):

    def setUp(self) -> None:
        self.plantation = Plantation(1)

    def test_correct_initialization(self):
        self.plants = {}
        self.workers = []
        self.assertEqual(1, self.plantation.size)
        self.assertEqual([], self.plantation.workers)
        self.assertEqual({}, self.plantation.plants)

    def test_plantation_size_incorrect_value_raise_error(self):

        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1

        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_successfully(self):
        result = self.plantation.hire_worker("Worker")

        self.assertEqual(["Worker"], self.plantation.workers)
        self.assertEqual("Worker successfully hired.", result)

    def test_hire_worker_not_successful_raise_error(self):
        self.plantation.workers = ["Worker"]
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Worker")

        self.assertEqual("Worker already hired!", str(ve.exception))
        self.assertEqual(["Worker"], self.plantation.workers)

    def test_return_correct_len_of_plants(self):
        self.plantation.plants = {"plant": ["type1", "type2"]}

        self.assertEqual(self.plantation.__len__(), 2)

    def test_planting_worker_not_existing_raise_error(self):
        self.plantation.hire_worker("Test")

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Worker", "plant")

        self.assertEqual(f"Worker with name Worker is not hired!", str(ve.exception))

    def test_planting_if_len_plant_gt_size_raise_error(self):
        self.plantation.size = 3

        self.plantation.hire_worker("Worker")

        self.plantation.planting("Worker", "plant")
        self. assertEqual(1, len(self.plantation))

        self.plantation.planting("Worker", "plant2")
        self.assertEqual(2, len(self.plantation))

        self.plantation.hire_worker("Worker2")
        self.plantation.planting("Worker2", "plant3")

        self.assertEqual({"Worker": ['plant', 'plant2'], "Worker2": ['plant3']}, self.plantation.plants)
        self.assertEqual(3, len(self.plantation))

    def test_planting_plantation_is_full_raise_error(self):
        self.plantation.hire_worker("Worker")
        self.plantation.size = 2
        self.plantation.plants = {"Worker": ["plant1", "plant2"]}

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Worker", "plant3")

        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_worker_plants_its_first_plant_correctly(self):
        self.plantation.workers = ["Worker"]
        self.plantation.plants = {}
        self.assertEqual(f"Worker planted it's first plant.", self.plantation.planting("Worker", "plant"))

    def test_planting_worker_plants_a_plant_correctly(self):
        self.plantation.workers = ["Worker"]
        self.plantation.plants = {"Worker": []}
        self.assertEqual("Worker planted plant.", self.plantation.planting("Worker", "plant"))

    def test_correct__str__(self):
        self.plantation.size = 3
        self.plantation.hire_worker("Worker")
        self.plantation.hire_worker("Worker2")
        self.plantation.planting("Worker", "plant1")
        self.plantation.planting("Worker2", "plant2")

        result = str(self.plantation)

        expected = f"Plantation size: 3\nWorker, Worker2\nWorker planted: plant1\nWorker2 planted: plant2"

        self.assertEqual(expected, result)

    def test_correct__repr__(self):
        self.plantation.size = 3
        self.plantation.hire_worker("Worker")
        self.plantation.hire_worker("Worker2")

        result = repr(self.plantation)

        expected = f'Size: 3\nWorkers: Worker, Worker2'

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()

