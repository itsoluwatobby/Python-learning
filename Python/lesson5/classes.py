class Vehicle:
    
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Moves along...')
    
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")
    
my_car = Vehicle('Tesla', 'Model 3')
# my_car.moves()
# print(my_car.make)
# my_car.get_make_model()

class Aeroplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id
    
    def get_make_model(self):
         print(f"I'm a {self.make} {self.model} with ID: {self.faa_id}.")
    
    def moves(self):
        print('Flies along')

class Truck(Vehicle):
    def moves(self):
        print('Rumbles along')

class GolfCart(Vehicle):
    pass

cessna = Aeroplane('Cessena', 'Skyhawk', '25444447AWQ5')
mark = Truck('Mark', 'Pinnacle')
golfwagon = GolfCart('Yamaha', 'GC100')

# cessna.get_make_model()
# cessna.moves()
# mark.get_make_model()
# mark.moves()
# golfwagon.get_make_model()
# golfwagon.moves()

# POLYMORPHISM
for v in (my_car, cessna, mark, golfwagon):
    v.get_make_model()
    v.moves()
    print('-------------------------------------')