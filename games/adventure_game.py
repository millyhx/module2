#ADVENTURE GAME#

#setting the scene
def first_chapter():
    print(">>>> CHAPTER ONE <<<<")
    print("")
    print("One night, two of your friends decided they wanted to cause some mischief.")
    print("You weren't sure on the idea thay had conjured up, but you didn't want to feel left out.")
    name = input("Enter your character name: ")
    print("")
    print("Marcus:  Come on {}, you never want to do anything fun!".format(name))
    print("Jade: Yeah, {}, you're so boring sometimes.".format(name))
    print("")
    print("------------")
    print("YOUR REPLY:")
    print("------------")
    print("I'm not going (1)")
    print("Fine, let's do this (2)")
    
    choice_ch1 = input("What's your choice?: ")
    if choice_ch1 == "1":
        print("Marcus:  I knew it. Bye, {}".format(name))
        print("Jade:  Yeah, me too. Bye, {}.".format(name))
    elif choice_ch1 == "2":
        second_chapter(name)
        


def second_chapter(name):
    print("")
    print(">>>> CHAPTER TWO <<<<")
    print("")
    print("Marcus:  Okay, first of all, where should we go? ")
    print("Jade: Please don't pick somewhere boring {}...".format(name))
    
    print("------------")
    print("YOUR REPLY:")
    print("------------")
    print("Abandoned house (1)")
    print("Creepy forest (2)")    
    
    choice_ch2 = input("What's your choice?: ")
    if choice_ch2 == "1":
        abandoned_house(name)
    elif choice_ch2 == "2":
        creepy_forest(name)
        
        
def abandoned_house(name):
    print("")
    print(">>>> THE ABANDONED HOUSE <<<<")
    print("")
    print("You, Marcus and Jade all walk to an abandoned house.")
    print("The house is quite faraway and you suggest to bring some items just in case you end up staying longer than you wanted too.")
    print("")
    print("List of Items: ")
    print("--------------")
    print("Hairbrush (a)")
    print("Torch (b)")
    print("Multi-purpose hammer (c)")
    print("Pack of haribos (d)")
    item = input("Enter an item from the list above that you think you'll need:  ")
    
    if item == "a":
        print("Marcus: Wow. A hairbush? Really? We're going to an abandoned house {}, not a fashion show.".format(name))
    elif item == "b":
        print("Jade: Good thinking {}.".format(name))
    elif item == "c":
        print("Marcus: That might actually come in handy, {}.".format(name))
    elif item == "d":
        print("Jade:  That's going to be really useful {}... let me have some?".format(name))
    


def creepy_forest(name):
    ...
first_chapter()

