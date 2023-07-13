class User():
    def __init__(self, firs_name, last_name, age, city, login_attempts):
        self.name = firs_name
        self.l_name = last_name
        self.age = age
        self.city = city
        self.login = login_attempts

    def describe_user(self):
        print(f'Name of user is: {self.name}')
        print(f'Last name of user is: {self.l_name}')
        print(f'Age of user is: {self.age}')
        print(f'User living in: {self.city}')
        print(f'Loging attempts is {self.login}')

    def greet_user(self):
        print(f'Hello {self.name} {self.l_name}!\n')

    def increment_login_atempts(self, atempts):
        self.login += atempts

    def reset_login_atempts(self):
        self.login = 0


class Admin(User):
    def __init__(self, firs_name, last_name, age, city, login_attempts):
        super().__init__(firs_name, last_name, age, city, login_attempts)
        self.privilages = ['Разрешено добавлять пользователей', 'Разрешено удалять пользователей',
                           'Разрешено банить пользователей']

    def show_privilages(self):
        for priv in self.privilages:
            print(f"Пользователь имеет приведегию: {priv}")


admin = Admin('John', 'Jones', 31, 'Ney-York', 0)

admin.describe_user()
admin.show_privilages()
