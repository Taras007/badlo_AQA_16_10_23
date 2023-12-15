import pytest
from object_service import ObjectService
from object_model import ObjectModel

service = ObjectService()

# Тести для GET LIST OF ALL OBJECTS
def test_get_all_objects_status_code():
    status_code, _ = service.get_all_objects()
    assert status_code == 200

def test_get_all_objects_response_length():
    _, objects = service.get_all_objects()
    assert len(objects) > 0

def test_get_all_objects_response_type():
    _, objects = service.get_all_objects()
    for obj in objects:
        assert isinstance(obj, ObjectModel)

def test_get_all_objects_response_content():
    _, objects = service.get_all_objects()
    for obj in objects:
        assert 'id' in obj.__dict__
        assert 'name' in obj.__dict__

# Тести для GET LIST OF OBJECTS BY IDS
def test_get_objects_by_ids_status_code():
    status_code, _ = service.get_objects_by_ids([3, 5, 10])
    assert status_code == 200

def test_get_objects_by_ids_response_length():
    _, objects = service.get_objects_by_ids([3, 5, 10])
    assert len(objects) == 3

def test_get_objects_by_ids_response_type():
    _, objects = service.get_objects_by_ids([3, 5, 10])
    for obj in objects:
        assert isinstance(obj, ObjectModel)

def test_get_objects_by_ids_response_content():
    _, objects = service.get_objects_by_ids([3, 5, 10])
    for obj in objects:
        assert obj.id in ["3", "5", "10"]

# Тести для GET SINGLE OBJECT
def test_get_single_object_status_code():
    status_code, _ = service.get_single_object(7)
    assert status_code == 200

def test_get_single_object_response_type():
    _, obj = service.get_single_object(7)
    assert isinstance(obj, ObjectModel)

def test_get_single_object_response_content():
    _, obj = service.get_single_object(7)
    assert obj.id == "7"
    assert obj.name == "Apple MacBook Pro 16"

def test_get_single_object_response_data():
    _, obj = service.get_single_object(7)
    assert 'year' in obj.data
    assert 'price' in obj.data

# Тести для POST: Додавання Об'єкта
def test_add_object_status_code():
    new_object_data = {
        "name": "Test Object",
        "data": {
            "detail": "Test Detail"
        }
    }
    status_code, _ = service.add_object(new_object_data)
    assert status_code == 200

def test_add_object_response_type():
    new_object_data = {
        "name": "Test Object",
        "data": {
            "detail": "Test Detail"
        }
    }
    _, obj = service.add_object(new_object_data)
    assert isinstance(obj, ObjectModel)

def test_add_object_response_content():
    new_object_data = {
        "name": "Test Object",
        "data": {
            "detail": "Test Detail"
        }
    }
    _, obj = service.add_object(new_object_data)
    assert obj.name == "Test Object"
    assert obj.data == new_object_data["data"]

# Тести для PUT: Оновлення Об'єкта
def test_update_object_status_code():
    updated_object_data = {
        "name": "Updated Object",
        "data": {
            "detail": "Updated Detail"
        }
    }
    status_code, _ = service.update_object(7, updated_object_data)
    assert status_code == 200

def test_update_object_response_content():
    updated_object_data = {
        "name": "Updated Object",
        "data": {
            "detail": "Updated Detail"
        }
    }
    _, obj = service.update_object(7, updated_object_data)
    assert obj.name == "Updated Object"
    assert obj.data == updated_object_data["data"]

# Тести для PATCH: Часткове Оновлення Об'єкта
def test_partially_update_object_status_code():
    partial_update_data = {"name": "Partially Updated Object"}
    status_code, _ = service.partially_update_object(7, partial_update_data)
    assert status_code == 200

def test_partially_update_object_response_content():
    partial_update_data = {"name": "Partially Updated Object"}
    _, obj = service.partially_update_object(7, partial_update_data)
    assert obj.name == "Partially Updated Object"

# Тести для DELETE: Видалення Об'єкта
def test_delete_object_status_code():
    status_code, _ = service.delete_object(6)
    assert status_code == 200

def test_delete_object_response_content():
    _, response = service.delete_object(6)
    assert "message" in response
    assert response["message"] == "Object with id = 6, has been deleted."
