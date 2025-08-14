class car:
    def __init__(self,color,brand,car_seats):
        self.color=color
        self.brand=brand
        self.numberofsits=car_seats

my_first_car=car("black","jaguar",2)
print("color:",my_first_car.color)
print("brand:",my_first_car.brand)
print("car_seats:",my_first_car.seat_number)