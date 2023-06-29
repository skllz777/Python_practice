def city_country(city, country):
    full_info = f'{city}, {country}'
    return full_info.title()
info_1 = city_country('madrid', 'spain')
info_2 = city_country('moscow', 'russia')
info_3 = city_country('athens', 'greece')
print(info_1)
print(info_2)
print(info_3)