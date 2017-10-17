for i in range(1,12):
    print(i)

#######################################################
vovwels = 0
consonants = 0

for letter in "hello":
    if letter.lower()  in "aeiou":
        vowels = vovwels + 1
    elif letter == " ":
        pass
    else:
        consonants = consonants +1

print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))

# for loops with dictionaries

students = {
    "male":["Tom","Josh","Joe","Randy"],
    "female":["Sarah","Kate","Samantha","Emma"]
    }

for key in students.keys():
    print(key) # male/female
    print(students[key]) #names
    
    #print all names with an a
    for name in students[key]:
        if "a" in name:
            print(name)
    
