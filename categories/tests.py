from rest_framework import test
from .models import Category
from users.models import User


class CategoryTestCase(test.APITestCase):
    base_url = "/api/v1/categories/"

    class UserTestData:
        username = "test1"
        password = "Example123$"

    class CategoryTestData:
        name = "Category Test"

    def setUp(self):
        Category.objects.create(name=self.CategoryTestData.name)

        admin_user = User.objects.create_superuser(
            username=self.UserTestData.username, password=self.UserTestData.password
        )
        admin_user.set_password(self.UserTestData.password)
        admin_user.save()
        self.admin_user = admin_user

    def test_get_all_categories(self):
        response = self.client.get(self.base_url)
        data = response.json()

        self.assertEqual(response.status_code, 200, "Status code is not 200")
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], self.CategoryTestData.name)

    def test_create_category(self):
        # If not logged in as admin user
        response = self.client.post(self.base_url)
        self.assertEqual(response.status_code, 403)

        # Error: Didn't providing necessary data
        self.client.force_login(self.admin_user)
        response_without_data = self.client.post(self.base_url)
        data = response_without_data.json()

        self.assertEqual(response_without_data.status_code, 400)

        # Successful
        response_after_login = self.client.post(
            self.base_url, data={"name": self.CategoryTestData.name}
        )
        data = response_after_login.json()

        self.assertEqual(
            response_after_login.status_code, 201, "Status code is not 201"
        )
        self.assertEqual(data["name"], self.CategoryTestData.name)
