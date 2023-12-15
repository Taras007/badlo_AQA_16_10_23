import requests
from object_model import ObjectModel

class ObjectService:
    BASE_URL = "https://api.restful-api.dev/objects"

    def get_all_objects(self):
        response = requests.get(self.BASE_URL)
        objects = [ObjectModel.from_json(obj) for obj in response.json()]
        return response.status_code, objects

    def get_objects_by_ids(self, ids):
        response = requests.get(self.BASE_URL, params={"id": ids})
        objects = [ObjectModel.from_json(obj) for obj in response.json()]
        return response.status_code, objects

    def get_single_object(self, object_id):
        response = requests.get(f"{self.BASE_URL}/{object_id}")
        object = ObjectModel.from_json(response.json())
        return response.status_code, object

    def add_object(self, object_data):
        response = requests.post(self.BASE_URL, json=object_data)
        return response.status_code, ObjectModel.from_json(response.json())

    def update_object(self, object_id, object_data):
        response = requests.put(f"{self.BASE_URL}/{object_id}", json=object_data)
        return response.status_code, ObjectModel.from_json(response.json())

    def partially_update_object(self, object_id, object_data):
        response = requests.patch(f"{self.BASE_URL}/{object_id}", json=object_data)
        return response.status_code, ObjectModel.from_json(response.json())

    def delete_object(self, object_id):
        response = requests.delete(f"{self.BASE_URL}/{object_id}")
        return response.status_code, response.json()
