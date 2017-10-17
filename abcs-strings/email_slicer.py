#variable[start:end:step]

word = 'helloworld how are you'
word[0:5:1] # just prints hello

word[5:] # returns world
word[5::2] # goes in steps of two, returns ol

# counting from the end

word[-2] # returns l

word[word.index('world')] # returns 5(w) because world starts at 5

word[word.index('llo'):word.index('world')]

word[word.index('world'):] # go from world to the end
