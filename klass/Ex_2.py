class User():
    def __init__(self, firs_name, last_name, age, city):
        self.name = firs_name
        self.l_name = last_name
        self.age = age
        self.city = city
    def describe_user(self):
        print(f'Name of user is: {self.name}')
        print(f'Last name of user is: {self.l_name}')
        print(f'Age of user is: {self.age}')
        print(f'User living in: {self.city}')
    def greet_user(self):
        print(f'Hello {self.name} {self.l_name}!\n')

user_1 = User('John', 'Jones', 31, 'Ney-York')
user_2 = User('Daniel', 'Cormier', 44, 'Florida')
user_3 = User('Khabib', 'Nurmagomedov', 34, 'Makhachkala')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()


