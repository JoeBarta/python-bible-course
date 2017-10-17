# get sentence from user
original = input("Please enter a sentence: ").strip().lower()

# split sentence into words
words = original.split()

# loop and convert into piglatin
new_words = []

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vovwel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)

# join words

output = " ".join(new_words)

# output 
print(output)
