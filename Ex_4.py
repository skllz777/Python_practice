guests = ['Billy', 'Andy', 'Leo', 'Luca']
guests.insert(0, 'Vova')
guests.insert(2, 'Ron')
guests.append('Karim')
print(f'{guests[0]}, I want to invite you on my birthday party')
print(f'{guests[1]}, I want to invite you on my birthday party')
print(f'{guests[2]}, I want to invite you on my birthday party')
print(f'{guests[3]}, I want to invite you on my birthday party')
print(f'{guests[4]}, I want to invite you on my birthday party')
print(f'{guests[5]}, I want to invite you on my birthday party')
print(f'{guests[6]}, I want to invite you on my birthday party')

print(', '.join(guests))