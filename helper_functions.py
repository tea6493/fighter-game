import myclass
import random

def play():
    print("Would you like to play?")
    if (response := str(input("press 'y' to start or 'n' to quit:"))) == "y":
        print("\n\nLet's begin!\n\n")
    elif response == "n":
        print("\n\nGood bye:)")
    else:
        print("\n\nThat is not a valid answer. Let's try again:))\n\n")
        response = play()
    return response

def game_mode():
    if (response := str(input("Which game mode would you like to play?\n1. Single Player\t\t2. Two Player (PVP)\t\t3. Game Mode Explanation\n\n:"))) == "1":
        return 1
    elif response == "2":
        return 2
    elif response == "3":
        print("\n\nIn single player mode, you will be fighting against a artificial opponent.\nIn a twoplayer mode, you get to player your friend!\n\n")
        response = str(input("Press enter to go back to selection\n:"))
        return game_mode()
    else:
        print("\n\nThat is not a valid answer. Let's try again:))\n\n")
        return game_mode()

def repeat_charact_desc():
    if (response := str(input("Would you like to know about different character? press 'y' to see other character or 'n' to go to character selection!"))) == "y":
        return character_desc()
    elif response == "n":
        return None
    else:
        print("\n\nThat is not a valid answer. Let's try again:))\n\n")
        return repeat_charact_desc()

def character_desc():
    if (response := str(input("Choose a character you want to know about!\n1. Rocky Jr.\t\t2. John Papel\t\t3. Harry Cutt\n:"))) == "1":
        print("\n\nRocky Jr. is a 'rock' type fighter from the Rocky Land, where everything there is rock. House... food... clothes... LIKE Everything! This caused his body to be rock solid which he uses it to become a world champion in boxing!\nHe can use 4 moves: 1. Punch 2. Throw Rock 3. Harden and 4. Taunt. He fights well in his child hood home town The Magnificent Canyon where he trained since when he was young.\n\n")
        print("1. punch: It is his basic attack. 90%\ chance to hit 2. Throw Rock : It is his stronger attack. 70%\ chance to hit and when he misses, he will hurt himself. 3. Harden : Increase Defense (80% \chance) 4. Taunt : Decrease enemy damage (50% \chance)")
    elif response == "2":
        print("\n\nJohn Papel is a 'paper' type fighter from the Scranton, Pennsylvania, the home land of Dunder Mifflin the paper company. His body is very big yet flexible. Although he is strong, he likes wrapping other people's gifts.\nHe can use 4 moves: 1. Punch 2. Paper Cut 3. meditation and 4. Story Writing. He fights well in The Grand Forest where he spends his time off making paper\n\n")
        print("1. punch: It is his basic attack. 90%\ chance to hit 2. Throw Rock : It is his stronger attack. 70%\ chance to hit and when he misses, he will hurt himself. 3. Meditation : Heal hp a little bit (80% \chance) 4. Story Writing : Transport to different map (50% \chance)")
    elif response == "3":
        print("\n\nHarry Cutt is a 'scissor' type fighter from the Wakanda, where the world's toughest metal 'Vibranium' comes from. He fights with the sharp armor and cut through enemies with no problem!\nHe can use 4 moves: 1. Punch 2. Chop Chop 3. Reflextion and 4. Sharpen. He fights well in The Metal Mine where he grab vibranium to add on to his armor.\n\n")
        print("1. punch: It is his basic attack. 90%\ chance to hit 2. Throw Rock : It is his stronger attack. 70%\ chance to hit and when he misses, he will hurt himself. 3. Reflextion : Decrease enemy defense (80% \chance) 4. Sharpen : Increase damage (50% \chance)")
    else:
        print("\n\nThat is not a valid answer. Let's try again:))\n\n")
        return character_desc()
    return repeat_charact_desc()

def character_selection():
    if (response := str(input("Who do you want to play as?\n1. Rocky Jr.\t\t2. John Papel\t\t3. Harry Cutt\n:"))) == "1":
        return myclass.Character("Rocky Jr.", "rock", 12, 6, 100, "Throw Rock")
    elif response == "2":
        return myclass.Character("John Papel", "paper", 10, 8, 110, "Paper Cut")
    elif response == "3":
        return myclass.Character("Harry Cutt", "scissor", 15, 5, 90, "Chop Chop")
    elif response == "4":
        return random.choice([myclass.Character("Rocky Jr.", "rock", 12, 6, 100, "Throw Rock"), myclass.Character("John Papel", "paper", 10, 8, 110, "Paper Cut"), myclass.Character("Harry Cutt", "scissor", 15, 5, 90, "Chop Chop")])
    else:
        print("\n\nThat is not a valid answer. Let's try again:))\n\n")
        return character_selection()

def rand_character_selection():
        return random.choice([myclass.Character("Rocky Jr.", "rock", 12, 6, 100, "Throw Rock"), myclass.Character("John Papel", "paper", 10, 8, 110, "Paper Cut"), myclass.Character("Harry Cutt", "scissor", 15, 5, 90, "Chop Chop")])

def repeat_map_desc():
    if (response := str(input("would you like to know about different map? press 'y' to see other map or 'n' to continue!\n:"))) == "y":
        return map_desc()
    elif response == "n":
        return None
    else:
        print("\n\nThat is not a valid answer. Let's try again:))\n\n")
        return repeat_map_desc()

def map_desc():
    if (response := str(input("\n\nWhich map do you want to know about?\n1. The Magnificent Canyon\t\t2. The Grand Forest\t\t3. The Metal Mine\n:"))) == "1":
        print("\n\nMagnificent Canyon is located in the center of the Rocky Land. It is a 'rock' type battle field. It gives locational advantages to Rocky Jr. but not so much to Harry Cutt.\n\n")
    elif response == "2":
        print("\n\nGrand Forest is located in the west of the Scranton, Pennsylvania. It is a 'paper' type battle field. It gives locational advantages to John Papel but not so much to Rocky Jr.\n\n")
    elif response == "3":
        print("\n\nMetal Mine is located in the east of the Wakanda. It is a 'scissor' type battle field. It gives locational advantages to Harry Cutt but not so much to John Papel.\n\n")
    else:
        print("\n\nThat is not a valid answer. Let's try again:))\n\n")
        return map_desc()
    return repeat_map_desc()

def map_selection():
    if (response := str(input("Which map do you want to play at?\n1. The Magnificent Canyon\t\t2. The Grand Forest\t\t3. The Metal Mine\t\t4. Random\n"))) == "1":
        return myclass.rock_map
    elif response == "2":
        return myclass.paper_map
    elif response == "3":
        return myclass.scissor_map
    elif response == "4":
        return random.choice([myclass.rock_map, myclass.paper_map, myclass.scissor_map])
    else:
        print("\n\nThat is not a valid answer. Let's try again:))\n\n")
        return character_selection()

def rand_map_selection():
     return random.choice([myclass.rock_map, myclass.paper_map, myclass.scissor_map])

def map_advantage(character_type, map_type):
    buffer = 0
    if character_type == "rock":
        if map_type == "rock":
            buffer = 5
        elif map_type == "scissor":
            buffer = -3

    elif character_type == "paper":
        if map_type == "paper":
            buffer = 5
        elif map_type == "rock":
            buffer = -3

    elif character_type == "scissor":
        if map_type == "scissor":
            buffer = 5
        elif map_type == "paper":
            buffer = -3

    return buffer

def what_move(character_type):
    print("Which move do you want to use?")
    if character_type == "rock":
        print("1.Punch\t\t2.Throw Rocks\t\t3.Harden\t\t4.Taunt")
        
    elif character_type == "paper":
        print("1.Punch\t\t2.Paper Cut\t\t3.Meditation\t\t4.Story Writing")
        
    elif character_type == "scissor":
        print("1.Punch\t\t2.Chop Chop\t\t3.Reflection\t\t4.Sharpen")
        

    if (response := str(input(":"))) == "1":
            return 1
    elif response == "2":
            return 2
    elif response == "3":
            return 3
    elif response == "4":
            return 4
    else:
        print("\n\nThat is not a valid answer. Let's try again:))\n\n")
        return what_move(character_type)

def fight(player, opponent, arena, move):
    buffer = map_advantage(player.character_type, arena.map_type)
    chance = random.randrange(0, 101, 10)
        
    if move == 1:
        print("%s used punch!" % (player.name))
        if chance <= 90:
            damage = player.damage + buffer
            if damage - opponent.defense <= 0:
                damage = 0
            else:
                damage - opponent.defense
            opponent.health -= damage
            print("%s did %d damage to %s. %s is now at %d hp point!\n" % (player.name, damage, opponent.name, opponent.name, opponent.health))
        else:
            print("%s missed.\n" % (player.name))
    elif move == 2:
        print("%s used %s!" % (player.name, player.move2))
        if chance <= 70:
            damage = (player.damage * 2) + buffer
            if damage - opponent.defense <= 0:
                damage = 0
            else:
                damage - opponent.defense
            opponent.health -= damage
            print("%s did %d damage to %s. %s is now at %d hp point!\n" % (player.name, damage, opponent.name, opponent.name, opponent.health))
        else:
            if player.damage > player.defense:
                player.health -= player.damage - player.defense
            print("%s missed and hurt him self. %s is now at %d hp point.\n" % (player.name, player.name, player.health))
    elif move == 3:
        if chance <= 80:
            if player.character_type == "rock":
                player.defense += 3
                print("%s used Harden. His defense increased to %d.\n" % (player.name, player.defense))
            elif player.character_type == "paper":
                if player.health + 5 >= 70:
                    player.health = 70
                else:
                    player.health += 5
                print("%s used meditation! He is now at %d hp point!\n" % (player.name, player.health))
            elif player.character_type == "scissor":
                if opponent.defense - 3 < 0:
                    opponent.defense = 0
                else:
                    opponent.defense -= 3
                print("%s used Reflextion! %s is blinded. %s's defense decreased to %d.\n" % (player.name, opponent.name, opponent.name, opponent.defense))
        else:
            print("%s missed.\n" % (player.name))

    elif move == 4:
        if chance <= 50:
            if player.character_type == "rock":
                if opponent.damage - 5 < 0:
                    opponent.damage = 0
                else:
                    opponent.damage -= 5
                print("%s used Taunt! %s's damage dropped to %d.\n" % (player.name, opponent.name, opponent.damage))
            elif player.character_type == "paper":
                arena = random.choice([myclass.rock_map, myclass.paper_map, myclass.scissor_map])
                print("%s used Story Writing! We were transported to %s which is %s type battle field.\n" % (player.name, arena.name, arena.map_type))
            elif player.character_type == "scissor":
                player.damage += 7
                print("%s used Sharpen! %s's damage increased to %d.\n" % (player.name, player.name, player.damage))
        else:
            print("%s missed.\n" % (player.name))

def single_player_fight(p1, p2, arena):
    print("%s will start with %d hp points and %s will start with %d hp points.\n" % (p1.name, p1.health, p2.name, p2.health))
    while p1.health > 0 and p2.health > 0:
        move = what_move(p1.character_type)
        fight(p1, p2, arena, move)
        if p1.health > 0 and p2.health > 0:
            move = random.randrange(1, 5, 1)
            fight(p2, p1, arena, move)
    if p1.health >= 0:
        print("%s fainted." % (p2.name))
        print("You win!\n\n")
    elif p2.health >= 0:
        print("%s fainted." % (p1.name))
        print("You lose:((\n\n")

def two_player_fight(p1, p2, arena):
    print("%s will start with %d hp points and %s will start with %d hp points.\n" % (p1.name, p1.health, p2.name, p2.health))
    while p1.health > 0 and p2.health > 0:
        move = what_move(p1.character_type)
        fight(p1, p2, arena, move)
        if p1.health > 0 and p2.health > 0:
            move = what_move(p2.character_type)
            fight(p2, p1, arena, move)
    if p1.health >= 0:
        print("%s fainted." % (p2.name))
        print("Player 1 wins!\n\n")
    elif p2.health >= 0:
        print("%s fainted." % (p1.name))
        print("Player 2 wins!\n\n")
