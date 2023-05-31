from rest_framework import test
from .models import RoomAmenity, Room
from users.models import User


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
