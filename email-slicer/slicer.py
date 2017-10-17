# get user email address
email = input('What is your enamil address:?').strip()

# slice out user name
user = email[:email.index('@')]

# slice domain anme
domain = email[email.index('@') + 1:]

# format message
output = 'Your username is {} and your domain is {}'.format(user, domain)

# display output message
print(output)
