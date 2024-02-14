import os

os.system("cls")


class SpaceAircraft:
    def __init__(self, model, height, fuel):
        self.model = model
        self.height = height
        self.fuel = fuel

    def launch(self, k):
        self.fuel -= launchFuel * k

    def land(self, k):
        self.fuel -= landFuel * k
        if self.fuel < 0:
            print("No fuel")
        else:
            print("SpaceAircraft")


launchFuel = float(input("Launch da 1 km uchun qancha fuel ketadi: "))
landFuel = float(input("Land da 1 km uchun qancha fuel ketadi: "))

raketa = SpaceAircraft(
    input("Model: "), int(input("Height: [metr] ")), float(input("Fuel: [list] "))
)

k = int(input("km: "))

k *= 1000

k -= raketa.height

k /= 1000

raketa.launch(k)
raketa.land(k)
