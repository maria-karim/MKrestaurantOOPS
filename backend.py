# backend.py

class User:
    def __init__(self, name):
        self.name = name

class Customer(User):
    def view_menu(self, menu):
        return menu

class Staff(User):
    def take_order(self, table, item):
        table.add_order(item)

class Manager(User):
    def add_menu_item(self, menu, category, item):
        if category in menu:
            menu[category].append(item)

class Table:
    def __init__(self, table_id, capacity, booked=False):
        self.table_id = table_id
        self.capacity = capacity
        self.__is_booked = booked
        self.orders = []

    def reserve_table(self):
        if not self.__is_booked:
            self.__is_booked = True
            return True
        return False

    def is_booked(self):
        return self.__is_booked

    def add_order(self, item):
        self.orders.append(item)

    def calculate_bill(self):
        return sum(item['price'] for item in self.orders)

class BookingSystem:
    def __init__(self):
        self.tables = [Table(i, 0, booked=(i <= 0)) for i in range(1, 11)]
        self.menu = {
            "Desi": [
                {"name": "Biryani", "price": 300, "icon": "🍗"},
                {"name": "Karahi", "price": 500, "icon": "🍖"}
            ],
            "Chinese": [
                {"name": "Chowmein", "price": 250, "icon": "🍜"},
                {"name": "Fried Rice", "price": 280, "icon": "🍚"}
            ],
            "Continental": [
                {"name": "Pizza", "price": 800, "icon": "🍕"},
                {"name": "Pasta", "price": 700, "icon": "🍝"}
            ],
            # "Bakery": [  # ❌ Hidden — No image yet
            #     {"name": "Cake", "price": 1000, "icon": "🎂"},
            #     {"name": "Samosa", "price": 50, "icon": "🥟"}
            # ]
        }

    def get_table(self, table_id):
        for table in self.tables:
            if table.table_id == table_id:
                return table
        return None

    def get_available_tables(self):
        return [t for t in self.tables if not t.is_booked()]
