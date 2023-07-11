class Restaurant():
    def __init__(self, restaurant_name, couisine_type):
        self.name = restaurant_name
        self.type = couisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f'Restaurant: {self.name}')
        print(f'Cousine: {self.type}')

    def restaurant_open(self):
        print(f'Restaurant {self.name} is opened')

    def set_number_served(self):
        print(f'Served persons is: {self.number_served}')
    def increment_number_served(self, served):
        self.number_served = served


restaurant = Restaurant('Millenium', 'European coisine')
restaurant.describe_restaurant()
restaurant.increment_number_served(122)
restaurant.set_number_served()
