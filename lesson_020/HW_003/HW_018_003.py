from abc import ABC, abstractmethod
import time

# Батьківські класи для блюд та напоїв
class Dish(ABC):
    @abstractmethod
    def serve(self):
        pass

class Drink(ABC):
    @abstractmethod
    def serve(self):
        pass

# Конкретні класи для різних блюд
class Risotto(Dish):
    def serve(self):
        return "Risotto is served!"

class Pasta(Dish):
    def serve(self):
        return "Pasta is served!"

class Pizza(Dish):
    def serve(self):
        return "Pizza is served!"

# Конкретні класи для напоїв
class Soda(Drink):
    def serve(self):
        return "Soda is served!"

class Juice(Drink):
    def serve(self):
        return "Juice is served!"

# Клас для отримання предметів замовлення
class OrderPartExtended:
    def get_item(self, item_name):
        items = {
            "Risotto": Risotto,
            "Pasta": Pasta,
            "Pizza": Pizza,
            "Soda": Soda,
            "Juice": Juice
        }

        if item_name in items:
            return items[item_name]()
        else:
            raise ValueError(f"{item_name} is not available.")

# Клас для управління замовленням
class Order:
    def __init__(self):
        self.timestamp = time.time()
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_order_summary(self):
        return [item.serve() for item in self.items]

# Приклад використання:
order = Order()
risotto = OrderPartExtended().get_item("Risotto")
order.add_item(risotto)
print(order.get_order_summary())