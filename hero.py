import random
class Hero:
    def __init__(self,name):
        self.name = name
        self.health = 100
        self.atkpower = 10
    
    def attack(self):
        damage = random.randint(0,self.atkpower)
        return damage
    def take_damage(self, damage):
        self.health = max(0,self.health - damage)
        print("put dmg stuff here")
    def is_alive(self):
        return self.health > 0