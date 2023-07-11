class Restaurant():
    def __init__(self, restaurant_name, cousine_type):
        self.name = restaurant_name
        self.type = cousine_type

    def describe_restaurant(self):
        print(f'Restaurant: {self.name}')
        print(f'Cousine: {self.type}')

    def restaurant_open(self):
        print(f'Restaurant {self.name} is opened')


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cousine_type):
        super().__init__(restaurant_name, cousine_type)
        self.flavousr = ['chokolate', 'cherry', 'melon']

    def getflavour(self):
        for fla in self.flavousr:
            print(f'We have souch flavours: {fla}')


kiosk = IceCreamStand('IceDreams', 'Ice-Cream')
kiosk.describe_restaurant()
kiosk.getflavour()

