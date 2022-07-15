class Character:
    def __init__(self, val):
        self.val = val
    
    def getVal(self):
        m1_dmg, m2_dmg, m3_dmg, m4_dmg, m5_dmg = 5, 10, 15, 20, 25
        if self.val == 1:
            name, characterType, m1, m2, m3, m4, m5 = "Aang", "air", "attack1.1", "attack1.2", "attack1.3", "attack1.4", "attack1.5"
        elif self.val == 2:
            name, characterType, m1, m2, m3, m4, m5 = "Zuko", "fire", "attack2.1", "attack2.2", "attack2.3", "attack2.4", "attack2.5"
        elif self.val == 3:
            name, characterType, m1, m2, m3, m4, m5 = "Katara", "water", "attack3.1", "attack3.2", "attack3.3", "attack3.4", "attack3.5"
        elif self.val == 4:
            name, characterType, m1, m2, m3, m4, m5 = "Toph", "earth", "attack4.1", "attack4.2", "attack4.3", "attack4.4", "attack4.5"
        elif self.val == 5:
            name, characterType, m1, m2, m3, m4, m5 = "Scott", "normal", "attack5.1", "attack5.2", "attack5.3", "attack5.4", "attack5.5"

        return name, characterType, m1, m1_dmg, m2, m2_dmg, m3, m3_dmg, m4, m4_dmg, m5, m5_dmg

class Map:
    def __init__(self, val):
        self.val = val
    
    def getVal(self):
        if self.val == 1:
            field_name, field_type = "air_place", "air"
        elif self.val == 2:
            field_name, field_type = "fire_place", "fire"
        elif self.val == 3:
            field_name, field_type = "water_place", "water"
        elif self.val == 4:
            field_name, field_type = "earth_place", "earth"
        elif self.val == 5:
            field_name, field_type = "normal_place", "normal"
        return field_name, field_type