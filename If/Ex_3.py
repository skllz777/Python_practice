names = ['Adam', 'Billy', 'Jon', 'admin', 'Suzan']
for name in names:
    if name == 'admin':
        print('Hello admin, would you like to see a status report')
    else:
        print(f'Hello {name}, thank you for loging in again')