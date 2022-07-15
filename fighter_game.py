import myclass
import random


def game():
    #welcoming
    print("\n\n\nWelcome to Avatar the Last Airbender fighter game!\n")

    #play or nah
    response = play() #function goes to line 23
    if response == "n":
        return None
    
    #player 1 champ select
    print("player 1! Pick your character!")
    p1_name, p1_type, p1_m1, p1_m1_dmg, p1_m2, p1_m2_dmg, p1_m3, p1_m3_dmg, p1_m4, p1_m4_dmg, p1_m5, p1_m5_dmg = characterSelection() #goes to line 35
    print("You selected", p1_name + "!\n", p1_name + " is", p1_type + " type!")
    
    #player 2 champ select
    print("player 2! Pick your character!")
    p2_name, p2_type, p2_m1, p2_m1_dmg, p2_m2, p2_m2_dmg, p2_m3, p2_m3_dmg, p2_m4, p2_m4_dmg, p2_m5, p2_m5_dmg = characterSelection() #goes to line 35
    print("You selected", p2_name + "!\n", p2_name + " is", p2_type + " type!")

    #map select
    print("Let's pick map now:))")
    field_name, field_type = mapSelection()

def play():
    print("Would you like to play?\n")
    response = str(input("press 'y' to start or 'n' to quit:"))
    if response == "y":
        print("\nLet's begin!\n")
    elif response == "n":
        print("\ngood bye:)\n")
    else:
        print("\noop thats not the right response silly:3 try again!\n")
        response = play()
    return response

def characterSelection():

    player_input = str(input("\
Who do you want to play as?\n\n\
1. Aang\t\t2. Zuko\t\t3. Katara\t4. Toph\t\t5. Sokka\n\n\
Type the number assigned to the character to pick them!:"))
    
    if player_input == "1":
        name, characterType, m1, m1_dmg, m2, m2_dmg, m3, m3_dmg, m4, m4_dmg, m5, m5_dmg = myclass.player_input.Character(1).getVal()
        return name, characterType, m1, m1_dmg, m2, m2_dmg, m3, m3_dmg, m4, m4_dmg, m5, m5_dmg
    
    elif player_input == "2":
        name, characterType, m1, m1_dmg, m2, m2_dmg, m3, m3_dmg, m4, m4_dmg, m5, m5_dmg = myclass.player_input.Character(2).getVal()
        return name, characterType, m1, m1_dmg, m2, m2_dmg, m3, m3_dmg, m4, m4_dmg, m5, m5_dmg
    
    elif player_input == "3":
        name, characterType, m1, m1_dmg, m2, m2_dmg, m3, m3_dmg, m4, m4_dmg, m5, m5_dmg = myclass.player_input.Character(3).getVal()
        return name, characterType, m1, m1_dmg, m2, m2_dmg, m3, m3_dmg, m4, m4_dmg, m5, m5_dmg
    
    elif player_input == "4":
        name, characterType, m1, m1_dmg, m2, m2_dmg, m3, m3_dmg, m4, m4_dmg, m5, m5_dmg = myclass.player_input.Character(4).getVal()
        return name, characterType, m1, m1_dmg, m2, m2_dmg, m3, m3_dmg, m4, m4_dmg, m5, m5_dmg
    
    elif player_input == "5":
        name, characterType, m1, m1_dmg, m2, m2_dmg, m3, m3_dmg, m4, m4_dmg, m5, m5_dmg = myclass.player_input.Character(5).getVal()
        return name, characterType, m1, m1_dmg, m2, m2_dmg, m3, m3_dmg, m4, m4_dmg, m5, m5_dmg

    else:
        print("That is not a valid character. no worries! Let's try again:))\n")
        name, characterType, m1, m1_dmg, m2, m2_dmg, m3, m3_dmg, m4, m4_dmg, m5, m5_dmg = characterSelection()
        return name, characterType, m1, m1_dmg, m2, m2_dmg, m3, m3_dmg, m4, m4_dmg, m5, m5_dmg

def mapSelection():
    map_input = str(input("Which map do you want to play at?\n\n\
1. air_place\t\t2. fire_place\t\t3. water_place\n\n\
4. earth_place\t\t5. normal_place\t\t6. random"))

    if map_input == "1":
        field_name, field_type = myclass.map_input.Map(1).getVal()
        return field_name, field_type
    elif map_input == "2":
        field_name, field_type = myclass.map_input.Map(2).getVal()
        return field_name, field_type
    elif map_input == "3":
        field_name, field_type = myclass.map_input.Map(3).getVal()
        return field_name, field_type
    elif map_input == "4":
        field_name, field_type = myclass.map_input.Map(4).getVal()
        return field_name, field_type
    elif map_input == "5":
        field_name, field_type = myclass.map_input.Map(5).getVal()
        return field_name, field_type
    elif map_input == "6":
        field_name, field_type = myclass.map_input.Map(random.randrange(1, 5, 1)).getVal()
        return field_name, field_type
    else:
        print("That is not a valid map. no worries! Let's try again:))\n")
        field_name, field_type = mapSelection()
        return field_name, field_type


def map_advantage():


def fight():
    p1_health = 50
    p2_health = 50


def calcPoints():


game()