class Restaurant():
    def __init__(self, restaurant_name, couisine_type):
        self.name = restaurant_name
        self.type = couisine_type
    def describe_restaurant(self):
        print(f'Restaurant: {self.name}')
        print(f'Cousine: {self.type}')

    def restaurant_open(self):
        print(f'Restaurant {self.name} is opened')

restaurant = Restaurant('Millenium', 'European coisine')
restaurant_1 = Restaurant('Ganesha', "Indian")
restaurant_2 = Restaurant('Traroria', 'Italian')
restaurant.describe_restaurant()
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()