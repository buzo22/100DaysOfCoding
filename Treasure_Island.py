print("Welcome to the Wakataari Island.")
print("Your mission is to locate the Crater.")

option1 = input("You are making a hike. Where do you want to go? Type 'up' or 'down'. ").lower()
if option1 == "up":
    option2 = input("You have come to the crater. There, you see nature. Type 'here' to indicate you made it. Type 'move' to keep moving. ").lower()

    if option2 == "here":
        option3 = input("You have made it to the crater unharmed. There is a helicopter waiting, but you have to say which direction it is. Which direction, 'left' or 'right'? ").lower()

        if option3 == "right":
            print("Sorry, You do not have a ride home. Game over.")
        elif option3 == "left":
            print("You made it, and your pilot is waiting!")
    else:
        print("Invalid input. Game over.")
else:
    print("There will be an eruption soon! Game over.")
