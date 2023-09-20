from project.trip import Trip

from unittest import TestCase, main

class TestTrip(TestCase):

    def setUp(self) -> None:
        self.trip = Trip(1000.0, 2, True)

    def test_correct_initialization(self):
        self.assertEqual(1000.0, self.trip.budget)
        self.assertEqual(2, self.trip.travelers)
        self.assertEqual(True, self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

    def test_travelers_setter_raise_error(self):

        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0

        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_is_family_setter_error(self):
        self.trip.travelers = 1
        self.trip.is_family = True
        self.assertEqual(False, self.trip.is_family)

    def test_book_a_trip_destination_not_valid_raise_error(self):
        result = self.trip.book_a_trip("USA")

        self.assertEqual('This destination is not in our offers, please choose a new one!', result)

    def test_book_a_trip_is_family_true_price_lowers(self):
        self.trip.budget = 15000
        result = self.trip.book_a_trip("Brazil")
        price = 6200 * self.trip.travelers
        total_price = price * 0.9
        self.assertEqual(11160, total_price)

    def test_book_a_trip_not_enough_budget_return_message(self):
        result = self.trip.book_a_trip("Brazil")

        self.assertEqual('Your budget is not enough!', result)

    def test_book_a_trip_successfully(self):
        self.trip.budget = 15000
        result = self.trip.book_a_trip("Brazil")
        self.assertEqual(f'Successfully booked destination Brazil! Your budget left is 3840.00', result)

    def test_booking_status_no_bookings_yet_returns_message(self):
        result = self.trip.booking_status()
        self.assertEqual(f'No bookings yet. Budget: 1000.00', result)

    def test_booking_status_returns_result(self):
        self.trip.budget = 20000
        result = self.trip.book_a_trip("Brazil")
        # result += self.trip.book_a_trip("Bulgaria")
        final = self.trip.booking_status()

        self.assertEqual(f"Booked Destination: Brazil\n"
                         f"Paid Amount: 11160.00\n"
                         f"Number of Travelers: 2\n"
                         f"Budget Left: 8840.00", final)


if __name__ == "__main__":
    main()
