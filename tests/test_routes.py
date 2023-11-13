import unittest
from bson import ObjectId
from fastapi.testclient import TestClient
from main import app


class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.setup_mock_data()

    def setup_mock_data(self):
        self.mock_property_data = {
            "_id": "655173da2dc03a60df817732",
            "name": "Propiedad de prueba",
            "price": 100000,
            "year": "2023-11-13T18:19:09.900Z",
            "id_owner": "1564"
        }

    async def test_create_property(self):
        property_data = {
                "name": "name",
                "address": "casa",
                "price": 1000,
                "year": "2023-11-13T18:19:09.900Z",
                "id_owner": "1564"
            }
        response = self.client.post("/property/", json=property_data)
        self.assertEqual(response.status_code, 201)
        response_json = response.json()
        self.assertIn("name", response_json)
        self.assertIn("address", response_json)
        self.assertIn("price", response_json)
        self.assertIn("year", response_json)

    async def test_read_all_properties(self):
        response = self.client.get("/property/")
        response_json = response.json()
        print(response_json)
        self.assertEqual(response.status_code, 200)
        self.assertIn("name", response_json)
        self.assertIn("address", response_json)
        self.assertIn("price", response_json)
        self.assertIn("year", response_json)

    async def test_read_property_by_id(self):
        item_id = '655173da2dc03a60df817732'
        tem_id_object = ObjectId(item_id)
        response = self.client.get(f"/property/{tem_id_object}",
                                   params=self.mock_property_data)
        self.assertEqual(response.status_code, 200)

    async def test_update_property(self):
        item_id = '655173da2dc03a60df817732'
        temp_id_object = ObjectId(item_id)
        updated_data = {
            "name": "Updated Name",
            "address": "Updated Address",
            "price": 2000,
            "year": "2023-11-13T18:19:09.900Z",
            "id_owner": "1564"
        }
        response = self.client.put(f"/property/{temp_id_object}",
                                   json=updated_data)
        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        self.assertEqual(response_json["name"], updated_data["name"])
        self.assertEqual(response_json["address"], updated_data["address"])
        self.assertEqual(response_json["price"], updated_data["price"])
        self.assertEqual(response_json["year"], updated_data["year"])

    async def test_delete_property(self):
        item_id = '655173da2dc03a60df817732'
        temp_id_object = ObjectId(item_id)
        response = self.client.delete(f"/property/{temp_id_object}")
        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        self.assertIn("message", response_json)
        self.assertEqual(response_json["message"],
                         "Property deleted successfully")

    async def test_create_upload_file(self):
        with open("path/to/test_file.txt", "rb") as file:
            files = {"file": ("test_file.txt",
                              file, "application/octet-stream")}
            response = self.client.post("/property_image/uploadfile/",
                                        files=files)
        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        self.assertIn("file_id", response_json)
        self.file_id = response_json["file_id"]

    async def test_read_file(self):

        if self.file_id is not None:
            response = self.client.get(f"/property_image/file/{self.file_id}")
            self.assertEqual(response.status_code, 200)

    async def test_read_nonexistent_file(self):
        response = self.client.get("/property_image/file/nonexistent_file_id")
        self.assertEqual(response.status_code, 404)
