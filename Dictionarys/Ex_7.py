cities = {
    'paris': {
        'country': 'france',
        'cityzens': 3000000,
        'fact': 'efils tower',
    },

    'athens': {
        'country': 'greece',
        'cityzens': 2500000,
        'fact': 'acropol',
    },

    'dubai': {
        'country': 'Uae',
        'cityzens': 1500000,
        'fact': 'burj khalifa',
    },
}
for city_name, city_info in cities.items():
    print(f"\ncity: {city_name.title()}")
    full_info = f"{city_info['country']} {city_info['cityzens']} {city_info['fact']}"
    print(f"\t full information: {full_info.title()}")