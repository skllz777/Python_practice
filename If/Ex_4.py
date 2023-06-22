current_users = ['Adam', 'Billy', 'Jon', 'Fil', 'Suzan', 'Kate']
current_users_lower = [c_user.lower() for c_user in current_users]
new_users = ['Oleg', 'Alex', 'Fil', 'Jim', 'kate', 'Leo']
for user in new_users:
    if user.lower() in current_users_lower:
        print(f"{user} is already exists,You need to choose other name")
    else:
        print(f"Ok, {user}, You can take this name")