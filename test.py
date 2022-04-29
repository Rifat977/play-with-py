class Car:
    name = ""
    color = ""

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def start(self):
        print("Starting the engine")

mycar = Car("Premio", "Nevi-Blue")
print(mycar.name)
print(mycar.color)

mycar.start()
