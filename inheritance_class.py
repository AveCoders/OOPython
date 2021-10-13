class Vehicle:
    def __init__(self, maker, model, colour, price):
        self.maker = maker
        self.model = model
        self.colour = colour
        self.price = price


class Car(Vehicle):
    def __init__(self, maker, model, colour, price, seats):
        super().__init__(maker, model, colour, price)
        self.seats = seats

class Industrial_Vehicle(Vehicle):
    def __init__(self, maker, model, colour, price, lifting_weight):
        super().__init__(maker, model, colour, price)
        self.lifting_weight = lifting_weight


class Forklift(Industrial_Vehicle):
    def __init__(self, maker, model, colour, price, lifting_weight):
        super().__init__(maker, model, colour, price, lifting_weight)

class Crane(Industrial_Vehicle):
    def __init__(self, maker, model, colour, price, lifting_weight):
        super().__init__(maker, model, colour, price, lifting_weight)


car1 = Car("Opel", "Mokka", "Black", 20000, 5)
forklift1 = Forklift("Honda", "fl1", "Brown", 15000, 5)
crane1 = Crane("Caterpillar", "cr1", "Yellow", 65000, 15)

print(car1.maker, car1.model, car1.colour, car1.price, car1.seats)
print(forklift1.maker, forklift1.model, forklift1.colour, forklift1.price, forklift1.lifting_weight)
print(crane1.maker, crane1.model, crane1.colour, crane1.price, crane1.lifting_weight)