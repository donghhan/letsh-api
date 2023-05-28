from rest_framework import test
from .models import RoomAmenity


class RoomAmenityTest(test.APITestCase):
    class TestData:
        name = "Amenity test"
        icon = "example.png"
        base_url = "/api/v1/rooms/amenities"

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
        input = {"name": "New amenity", "icon": "new_icon.png"}
        response = self.client.post(
            self.TestData.base_url,
            data=input,
        )
        data = response.json()

        self.assertEqual(response.status_code, 200, "Status code is not 200")
        self.assertEqual(data["name"], input["name"])
        self.assertEqual(data["icon"], input["icon"])
