import helper_functions

def main():
    print("\n\n\nWelcome to worlds greatest rock, scissor, paper ultimate fighter game!\n\n")
    if (response := helper_functions.play()) == "n":
        return None

    if (response := helper_functions.game_mode()) == 1:
        print("\n\nYou selected Single Player!\n\n")
        single_player()
    elif response == 2:
        print("\n\nYou selected Two Player (PVP)!\n\n")
        pvp()
    
    print("\n\nThank you for Playing!")
    print("\n\nGood Bye!")

def single_player():
    if (response := str(input("Before we begin, do you need character description?\nPress 'y' to see the description or enter to continue!\n:\n"))) == "y":
        helper_functions.character_desc()

    print("Let's pick your character!\n\n")
    p1 = helper_functions.character_selection()
    print("\n\nYou selected ", p1.name + " who is ", p1.character_type + " type!\n\n")

    print("Picking your opponent. . . . . . .\n")
    p2 = helper_functions.rand_character_selection()
    print("You are going against ", p2.name + " who is ", p2.character_type + " type!\n\n")

    if (response := str(input("Next, Do you need map description?\nPress 'y' to see the description or enter to continue!\n:"))) == "y":
        helper_functions.map_desc()
    
    print("\n\nRandomely selecting a map . . . . . .\n")
    arena = helper_functions.rand_map_selection()
    print("You are going to play in the ", arena.name + " which is ", arena.map_type + " type!\n\n")

    print("Now... Let the Fight BEGIN!!\n\n")

    helper_functions.single_player_fight(p1, p2, arena)

    print("Would you like to play again?")
    if (response := str(input("press 'y' to start or enter to quit:"))) == "y":
        print("\n\nLet's begin!\n\n")
        single_player()

def pvp():
    if (response := str(input("Before we begin, do you need character description?\nPress 'y' to see the description or enter to continue!\n:\n"))) == "y":
        helper_functions.character_desc()

    print("Player 1! Let's pick your character!\n\n")
    p1 = helper_functions.character_selection()
    print("Player 1 selected ", p1.name + " who is ", p1.character_type + " type!\n\n")

    print("Player 2! Let's pick your character!\n\n")
    p2 = helper_functions.character_selection()
    print("Player 2 selected ", p2.name + " who is ", p2.character_type + " type!\n\n")

    if (response := str(input("Next, we have to pick a map. Do you need map description?\nPress 'y' to see the description or enter to continue!\n:"))) == "y":
        helper_functions.map_desc()
    
    print("\n\nLet's pick a map!")
    arena = helper_functions.map_selection()
    print("You guys are going to play in the ", arena.name + " which is ", arena.map_type + " type!\n\n")

    print("Now... Let the Fight BEGIN!!\n\n")

    helper_functions.two_player_fight(p1, p2, arena)

    print("Would you like to play again?")
    if (response := str(input("press 'y' to start or enter to quit:"))) == "y":
        print("\n\nLet's begin!\n\n")
        pvp()

main()
