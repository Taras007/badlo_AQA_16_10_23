import sys
import pytest


sys.path.append(r"C:\Users\Administrator\PycharmProjects\badlo_AQA_16_10_23\lesson_017")

from lesson_017.HW_016_001 import Train, TrainCar

@pytest.fixture
def train():
    return Train("London;York;Newcastle;Gogwarts")

# Фікстура для створення вагона з максимальною ємністю
@pytest.fixture
def train_car():
    return TrainCar(10)

# Smoke tests
@pytest.mark.smoke
def test_train_initialization(train):
    assert train.current_station_index == 0
    assert train.direction == 1
    assert train.route == "London;York;Newcastle;Gogwarts"

@pytest.mark.smoke
def test_train_car_initialization(train_car):
    assert train_car.car_number == TrainCar.car_number - 1
    assert train_car.max_capacity == 10
    assert train_car.passengers == []

# Regression tests
@pytest.mark.regression
def test_add_car(train):
    train.add_car(10)
    assert len(train) == 1  # Using the __len__ method of Train class

@pytest.mark.regression
def test_add_passenger(train, train_car):
    train.add_car(10)
    train.add_passenger(0, 1, "John Dow", "York", 1)
    assert train.cars[0].passengers[0]['passenger_name'] == "John Dow"

@pytest.mark.parametrize("station_index, car_number, passenger_name, destination, place, expected_name", [
    (0, 1, "John Dow", "York", 1, "John Dow"),
    (0, 1, "Emma Stone", "Newcastle", 2, "Emma Stone"),
    (0, 1, "Harry Potter", "Gogwarts", 3, "Harry Potter")
])
@pytest.mark.regression
def test_add_passenger_parameterized(train, station_index, car_number, passenger_name, destination, place, expected_name):
    train.add_car(10)
    train.add_passenger(station_index, car_number, passenger_name, destination, place)
    added_passenger_name = train.cars[car_number - 1].passengers[-1]['passenger_name']
    assert added_passenger_name == expected_name

@pytest.mark.regression
def test_move_to_next_station(train):
    initial_station_index = train.current_station_index
    train.move_to_next_station()
    assert train.current_station_index != initial_station_index
