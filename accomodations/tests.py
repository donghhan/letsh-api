from rest_framework.test import APITestCase
from .models import *
from users.models import User


class TestAmenitiesView(APITestCase):
    NAME = "Sample Amenity"
    DESCRIPTION = "This is a sample amenity for testing."

    def setUp(self):
        Amenity.objects.create(name=self.NAME)

    def test_all_amenities(self):
        response = self.client.get("/en/api/v1/accomodations/amenities/")
        data = response.json()
        print(data)

        self.assertEqual(response.status_code, 200, "Status code is not 200")
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], self.NAME)
        self.assertEqual(data[0]["description"], self.DESCRIPTION)


class TestAmenityView(APITestCase):
    PK = 1
    NAME = "Sample Amenity"
    DESCRIPTION = "This is a sample amenity for testing."

    def setUp(self):
        Amenity.objects.create(name=self.NAME, description=self.DESCRIPTION, pk=self.PK)

    def test_amenity_not_found(self):
        response = self.client.get("/en/api/v1/accomodations/amenities/2")
        self.assertEqual(response.status_code, 404)

    def test_get_amenity(self):
        response = self.client.get("/en/api/v1/accomodations/amenities/1")
        self.assertEqual(response.status_code, 200)
        data = response.json()

        self.assertEqual(data["name"], self.NAME)

    def test_put_amenity(self):
        pass

    def test_delete_amenity(self):
        response = self.client.delete("/en/api/v1/accomodations/amenities/1")

        self.assertEqual(response.status_code, 200)


class TestRooms(APITestCase):
    def setUp(self):
        user = User.objects.create(
            email="test@test.com",
            first_name="example_first_name",
            last_name="example_last_name",
            nickname="example_name",
        )
        user.set_password("example123")
        user.save()
        self.user = user

    def test_create_room(self):
        response = self.client.post("/en/api/v1/accomodations/")

        self.assertEqual(response.status_code, 403)

        self.client.login(email="test@test.com", password="example123")
        response = self.client.post("/en/api/v1/accomodations/")
        print(response)
