# python standard library to checkout functions

# ask not a name
name = input('What is your name?: ')
# ask for age
age = input('what is your age?: ')
# ask user for city
city = input('What city do you live in?: ')
# ask what they enjoy
love = input('What do you love doing?: ')
# create output text
string = 'Your name is {} and you are {} years old. You line in {} and you love {}'
output = string.format(name, age, city, love)
# print output to screen
print(output)
