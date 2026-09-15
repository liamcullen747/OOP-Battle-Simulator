import random
class Hero:
    def __init__(self,name):
        self.name = name
        self.health = 125
        self.attack_power = 20
    
    def attack(self):
        chance = random.randint(1,5)
        if chance == 1:
            damage = random.randint(self.attack_power, self.attack_power * 2)
            critical_hit = True
        else:
            damage = random.randint(0,self.attack_power)
            critical_hit = False
        return damage, critical_hit
    def take_damage(self, damage):
        self.health = max(0,self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")
    def is_alive(self):
        return self.health > 0