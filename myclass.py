class Character:
    def __init__(self, name, character_type, damage, defense, health, move2):
        self.name = name
        self.character_type = character_type
        self.damage = damage
        self.defense = defense
        self.health = health
        self.move2 = move2

class Map:
    def __init__(self, name, map_type):
        self.name = name
        self.map_type = map_type

rock_map = Map("The Magnificent Canyon", "rock")
paper_map = Map("The Grand Forest", "paper")
scissor_map = Map("The Metal Mine", "scissor")

