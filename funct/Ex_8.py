def user_id(first, last, **info):
    info['first_name'] = first
    info['last_name'] = last
    return info

user_profile = user_id('Cristiano', 'Ronaldo',
                       location='Portugal', profession='Fotball player')
print(user_profile)