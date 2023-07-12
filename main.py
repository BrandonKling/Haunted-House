# This program is for demonstrating functions and data entry. Brandon Kling 6/22/2023

#text based horror adventure game
#user will be given a scenario and will have to make a choice
#based on their choice, they will be given a different scenario

#print out title of game
print("\n\n*** Welcome to the Haunted House! ***")

# game function
def play_game(name):

    #print out to welcome user
    print(f"\nThank you, {name}! Now our journey begins...")

    #scenario one print out and if/else statement
    def scenario_one():
        print(f"\n\n{name}, you wake up in a dimly lit room. There are two doors in front of you.")
        print("What do you do?")
        print("1. Open the left door.")
        print("2. Open the right door.")
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            scenario_two()
        elif choice == "2":
            scenario_three()
        else:
            print("Invalid choice. Please try again.")
            scenario_one()

    #scenario two print out and if/else statement
    def scenario_two():
        print("\n\nYou open the left door and enter a long corridor.")
        print("There's a faint sound coming from the end of the corridor.")
        print("What do you do?")
        print("1. Follow the sound.")
        print("2. Turn back and go through the right door.")
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            scenario_four()
        elif choice == "2":
            scenario_five()
        else:
            print("Invalid choice. Please try again.")
            scenario_two()

    #scenario three print out and if/else statement
    def scenario_three():
        print("\n\nYou open the right door and find yourself in a small, eerie room.")
        print("There's a rusty key on the floor.")
        print("What do you do?")
        print("1. Pick up the key.")
        print("2. Ignore the key and leave the room.")
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            scenario_six()
        elif choice == "2":
            scenario_seven()
        else:
            print("Invalid choice. Please try again.")
            scenario_three()

    #scenario four print out and if/else statement
    def scenario_four():
        print("\n\nYou follow the sound and reach a room with a flickering candle.")
        print("There's a note on the table.")
        print("What do you do?")
        print("1. Read the note.")
        print("2. Examine the candle.")
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            scenario_eight()
        elif choice == "2":
            ending_two()
        else:
            print("Invalid choice. Please try again.")
            scenario_four()

    #scenario five print out and if/else statement
    def scenario_five():
        print("\n\nYou turn back and go through the right door.")
        print("You find yourself in a dark cellar with a staircase leading down.")
        print("What do you do?")
        print("1. Descend the staircase.")
        print("2. Go back and explore the previous room.")
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            ending_three()
        elif choice == "2":
            scenario_two()
        else:
            print("Invalid choice. Please try again.")
            scenario_five()

    #scenario six print out and if/else statement
    def scenario_six():
        print("\n\nYou pick up the key and hear a distant scream.")
        print("Suddenly, the room starts shaking.")
        print("What do you do?")
        print("1. Run towards the left door.")
        print("2. Run towards the right door.")
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            ending_four()
        elif choice == "2":
            ending_four()
        else:
            print("Invalid choice. Please try again.")
            scenario_six()

    #scenario seven print out and if/else statement
    def scenario_seven():
        print("\n\nYou leave the room and enter a hallway.")
        print("The hallway stretches in both directions.")
        print("What do you do?")
        print("1. Go left.")
        print("2. Go right.")
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            ending_six()
        elif choice == "2":
            ending_six()
        else:
            print("Invalid choice. Please try again.")
            scenario_seven()

    #scenario eight print out and if/else statement
    def scenario_eight():
        print("\n\nYou read the note, and it says, 'Beware the shadows.'")
        print("Suddenly, the candle goes out.")
        print("What do you do?")
        print("1. Light the candle.")
        print("2. Feel your way through the darkness.")
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            ending_five()
        elif choice == "2":
            ending_one()
        else:
            print("Invalid choice. Please try again.")
            scenario_eight()

    #ending one print out
    def ending_one():
        print(f"\n\n{name}, you made it through the horrors and find yourself outside the haunted house.")
        print("Congratulations! You have escaped the nightmare.")
        play_again()

    #ending two print out
    def ending_two():
        print(f"\n\n{name}, you are devoured by the shadows.")
        print("Congratulations! You have been consumed by the nightmare.")
        play_again()

    #ending three print out
    def ending_three():
        print(f"\n\n{name}, as you descend the staircase you notice hundreds of tiny eyes peering up at you...")
        print("You are devoured by the rats!")
        print("Congratulations! You have been consumed by the rats!")
        play_again()

    #ending four print out
    def ending_four():
        print(f"\n\n{name}, you run to the door and it slams shut!")
        print("You are trapped in the haunted house forever!")
        print("Congratulations! You have been trapped in an enchanted room and turned into an ottoman.")
        play_again()

    #ending five print out
    def ending_five():
        print(f"\n\n{name}, as you light the candle you notice a ghostly figure in the corner of the room.")
        print("The ghostly figure flies towards you at blinding speed and you are consumed by the shadows.")
        print("Congratulations! You have been consumed by the nightmare.")
        play_again()

    #ending six print out
    def ending_six():
        print(f"\n\n{name}, you look left and right and notice the hallway is endless.")
        print("You hear a sliding sound and notice the walls are closing in on you.")
        print("You are crushed by the walls!")
        print("Congratulations! You are now a pancake!")
        play_again()

    #allow the player to play again
    #if the player chooses yes, the game will start over
    #if the player chooses no, the game will end
    def play_again():
        choice = input("\nDo you want to play again? (y/n): ")
        if choice.lower() == "y":
            scenario_one()
        elif choice.lower() == "n":
            print(f"\n{name}, thank you for playing! Goodbye.")
        else:
            print("\nInvalid choice. Please try again.")
            play_again()

    #secret challenge print out
    def secret_challenge():
        print(f"\nCongratulations, {name}! You have achieved all possible endings in a single play session.")
        print("As a reward, you have acheived the title of No-Lifer!")

    # Start the game
    scenario_one()

     # Check if all endings were achieved
    all_endings = set([ending_one, ending_two, ending_three, ending_four, ending_five, ending_six])
    achieved_endings = set([ending_one, ending_two, ending_three, ending_four, ending_five, ending_six])

    # If all endings were achieved, the player will be rewarded with a secret challenge title
    if achieved_endings == all_endings:
        secret_challenge()

# Start the game loop
# This allows the player to start fresh and enter a new name
while True:
    #print out to take users name
    name = input("\nWhat is your name? ")
    play_game(name)
    choice = input("\nDo you want to quit the game? (y/n): ")
    if choice.lower() == "y":
        break
    elif choice.lower() == "n":
        continue
    else:
        print("\nInvalid choice. Exiting the game.")
        break