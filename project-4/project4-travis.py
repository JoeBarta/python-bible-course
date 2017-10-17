known_users = ["Joe", "Rene", "Samuel", "Jan", "James", "Josh"]

print(len(known_users))

while True:
    print("Hi! my name is Travis")
    name = input("What is your name?:").strip().capitalize()
    
    if name in known_users:
        print("Hello {}".format(name))
        remove = input("Would you like to be removed from the system *y/n)?:").lower
        
        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("No problem, I didn't want to anyway")
            
    else:
        print("I do not recognize you {}".format(name))
        add_me = input("Would you like to be added to the system (y/n)?:").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print("no worries, see you around!")


