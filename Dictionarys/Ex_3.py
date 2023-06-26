fav_languges = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'bob': 'java',
}
peoples = ['jen', 'phil', 'jon', 'ron', 'bob', 'mike']
for people in peoples:
    if people in fav_languges.keys():
        print(f"Thank you {people.title()}, for coming")
    else:
        print(f"{people.title()}, you need to come!")