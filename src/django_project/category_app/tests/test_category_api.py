from django.test import TestCase
from rest_framework.test import APITestCase 

class TestCategoryAPI(TestCase):
    def test_list_categories(self):
        url= "/api/categories/"
        response = self.client.get(url)

        
        expected_data = [
            {
                "id":"8227aa2b-6098-43d5-82e8-debd9536785b",
                "name":"Movie",
                "description":"Movie descritption",
                "is_active": True
            },
            {
                "id":"4c01e326-25af-44ee-9d0c-ea6a6b454e3b",
                "name":"Documentary",
                "description":"Documentary descritption",
                "is_active": True
            },
        ]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_data)

