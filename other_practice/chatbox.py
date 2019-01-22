
def simple_chatbox():
    name = input("What's your name? ")
    age = input("How old are you? ")
    print("{} is a good age, {}".format(age, name))
    print("---------------------------")
    choice = input("Do you want to know something? ")
    if choice == "yes":
        print("Milly loves {}".format(name))
    else:
        print("Oh, okay {}".format(name))
    print("---------------------------")
    print("One more thing... ")
    print("THIS PROJECTOR IS SO COOL")  
    

simple_chatbox()
