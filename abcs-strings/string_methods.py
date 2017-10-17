text = 'happy'
text.count('a')

'hello'.count('e')

text.count('day') # returns 1

x = 'HAPPY'
x.lower() # returns lowercase happy
x.upper() 
x.capitalize # caps the start letter
x.title() # capitalizes every word 

x.islower() # returns false since it is not lower case
# vice versa for all the other ones
x.isalpha() # whether everything in x is letters
# returns false since it counts the space as well

x.isdigit() # to check whether it contains only numbers

isalnum() # chars a-z and numbs 0-9

# counting

x = 'happy birthday'
x.index('birthday') # returns 6, starts at 0 so happy is 0-4, space is 5
# and then birthday begins

x.find('birthday') # also returns 6, however when searching for
# things tnhat doen't exist it doesn't crash
so x.find('gagfdsfs') # a string that doest exist
# just returns -1
# BOTH METHODS ARE CASE SENSITIVE

y = '000000000happybirthday00000
y.strip('0') # removes all the zeros to give us happybirthday
y.lstrip('0') #removes lefthand side 0s
y.rstrip('0') #removes righthand side 0s

y.strip() # still works, takes away all spaces
