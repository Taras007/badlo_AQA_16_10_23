class TrainCar:
    car_number = 1  # Початковий номер вагону

    def __init__(self, max_capacity):
        self.car_number = TrainCar.car_number
        TrainCar.car_number += 1
        self.passengers = []  # Список пасажирів в вагоні
        self.max_capacity = max_capacity  # Максимальна кількість пасажирів в вагоні

    def add_passenger(self, passenger_name, destination, place):
        if len(self.passengers) < self.max_capacity:
            self.passengers.append({
                "passenger_name": passenger_name,
                "destination": destination,
                "place": place
            })
        else:
            print("Вагон заповнений, не можна додати ще пасажира")

    def __str__(self):
        car_info = [f'"traincart": "{self.car_number}"']
        for passenger in self.passengers:
            car_info.append(f'"passenger_name": "{passenger["passenger_name"]}",')
            car_info.append(f'"destination": "{passenger["destination"]}",')
            car_info.append(f'"place": {passenger["place"]}')
        return "\n".join(car_info)

class Train:
    def __init__(self, route):
        self.route = route
        self.stations = route.split(";")  # Міста розділені ";"
        self.stations_dict = {i: station for i, station in enumerate(self.stations)}
        self.cars = []
        self.direction = 1  # 1 - вперед, -1 - назад
        self.current_station_index = 0

    def add_car(self, max_capacity):
        car = TrainCar(max_capacity)
        self.cars.append(car)

    def add_passenger(self, station_index, car_number, passenger_name, destination, place):
        try:
            station_name = self.stations_dict.get(station_index)
            if not station_name:
                print("Невірний індекс станції.")
                return

            if station_name == destination:
                print("Пасажир вже знаходиться на кінцевій станції.")
                return

            car = self.cars[car_number - 1]
            car.add_passenger(passenger_name, destination, place)
        except IndexError:
            print("Вагон з вказаним номером не існує.")

    def change_direction(self):
        self.direction *= -1  # Змінити напрямок руху

    def move_to_next_station(self):
        self.current_station_index += self.direction

        # Перевірка, чи дійшли до кінця маршруту і зміна напрямку
        if self.current_station_index < 0:
            self.current_station_index = 1
            self.change_direction()
        elif self.current_station_index >= len(self.stations):
            self.current_station_index = len(self.stations) - 2
            self.change_direction()

    def __len__(self):
        return len(self.cars)

    def __str__(self):
        return f"Train with {len(self.cars)} cars, direction: {'Forward' if self.direction == 1 else 'Backward'}, current station: {self.stations[self.current_station_index]}"

# Приклад використання:
train = Train("London;York;Newcastle;Gogwarts")
train.add_car(10)

# Додавання пасажирів до вагонів
train.add_passenger(0, 1, "John Dow", "York", 1)
train.add_passenger(2, 1, "Alex Dowson", "Gogwarts", 2)

# Переміщення потягу та вивід інформації про нього
train.move_to_next_station()
print(train)
train.move_to_next_station()
print(train)