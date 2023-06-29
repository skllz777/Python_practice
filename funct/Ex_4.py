def make_album(name, album, track = None):
    if track:
        full_info = {'first': name, 'last': album, 'third': track}
    else:
        full_info = {'first': name, 'last': album}
    return full_info
first_a = make_album('Basta', 'Noggano')
second_a = make_album('Rihanna', 'A girl like me', 5)
third_a = make_album('Eminem', 'infinite')
print(first_a)
print(second_a)
print(third_a)
