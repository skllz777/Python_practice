def city_country(city, country):
    full_info = f'{city}, {country}'
    return full_info.title()


while True:
    print("Please enter information: ")
    print("If you want to quit, enter 'q'")

    city_name = input("Enter city name: ")
    if city_name == 'q':
        break

    count_name = input("Enter country: ")
    if count_name == 'q':
        break

    information = city_country(city_name, count_name)
    print(f"Here your info: {information}")
