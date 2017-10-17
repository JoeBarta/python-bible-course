films = {
    "Bladerunner 2049":[15,5],
    "Wonder Woman":[12,2],
    "Dunkirk":[15,4],
    "Baby Driver 2049":[15,9]
    }
    
while True:
    choice = input("What film would you like to watch?:").strip().title()

    if choice in films:
        age = int(input("How old are you?:").strip())
                  
        if age >= films[choice][0]:

            num_seats = films[choice][1]
            if num_seats > 0:
                  print("Enjoy the film")
                  films[choice][1] = films[choice][1] - 1
            else:
                  print("Sorry, we are sold out!")
                  
        else:
            print("You are too young to see that film")
                  
    else:
        print("We Don't have that film")
