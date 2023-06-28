from rest_framework import test
from .models import RoomAmenity, Room
from users.models import User
from categories.models import Category
from reservations.models import Reservation


class RoomAmenityTest(test.APITestCase):
    class TestData:
        name = "Amenity test"
        icon = "example.png"
        base_url = "/api/v1/rooms/amenities/"

    def setUp(self):
        RoomAmenity.objects.create(name=self.TestData.name, icon=self.TestData.icon)

    def test_get_all_amenities(self):
        response = self.client.get(self.TestData.base_url)
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Status code is not 200",
        )
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], self.TestData.name)

    def test_create_new_amenities(self):
        pass


class RoomTest(test.APITestCase):
    class UserTestData:
        username = "test1"
        password = "Example123$"

    class TestData:
        name = "Test Room"
        price_per_night = 100
        guest = 4
        base_url = "/api/v1/rooms/"
        # User

    def setUp(self):
        # Room.objects.create(
        #     name=self.TestData.name,
        #     price_per_night=self.TestData.price_per_night,
        #     guest=self.TestData.guest,
        # )

        user = User.objects.create(username=self.UserTestData.username)
        user.set_password(self.UserTestData.password)
        user.save()
        self.user = user

    def test_get_all_rooms(self):
        pass

    def test_create_room(self):
        response = self.client.post(self.TestData.base_url)
        self.assertEqual(response.status_code, 403)

        self.client.force_login(self.user)
        response_after_login = self.client.post(self.TestData.base_url)


class RoomReservationTest(test.APITestCase):
    base_url = "/api/v1/rooms/2/reservations/"
    base_url_not_found = "/api/v1/rooms/199/reservations/"

    class UserTestData:
        username = "test"
        password = "Example123$"

    class RoomTestData:
        name = "test room"
        price_per_night = 100
        guest = 4

    class ReservationTestData:
        room = "test room"
        adult = 2
        children = 2
        check_in = "2023-06-15"
        check_out = "2023-06-30"

    def setUp(self):
        # Guest for booking room
        guest = User.objects.create(username=self.UserTestData.username)
        guest.set_password(self.UserTestData.password)
        guest.save()
        self.guest = guest

        # OWner of room
        owner = User.objects.create(username="owner")
        owner.set_password("Example123$")
        owner.save()
        self.owner = owner

        # Category of room
        category = Category.objects.create(name="test category")
        category.save()
        self.category = category

        room_to_book = Room.objects.create(
            name=self.RoomTestData.name,
            price_per_night=self.RoomTestData.price_per_night,
            guest=self.RoomTestData.guest,
            owner=owner,
            category=category,
        )

        Reservation.objects.create(
            guest=self.guest,
            room=room_to_book,
            adult=self.ReservationTestData.adult,
            children=self.ReservationTestData.children,
            check_in=self.ReservationTestData.check_in,
            check_out=self.ReservationTestData.check_out,
        )

    def test_get_reservation(self):
        response_not_found = self.client.get(self.base_url_not_found)

        # Check GET request for a single reservation
        self.assertEqual(response_not_found.status_code, 404)

        # Check if reservation is found
        self.client.force_login(self.guest)
        response = self.client.get(self.base_url)
        print(response)
