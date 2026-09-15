from goblin import Goblin
import goblin
from hero import Hero
import hero


ARENA_NAME = "The Ring of Doom and Despair"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Scary Alex")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    goblinTwo = Goblin("Scribble")

    hero = Hero("Knight")
    print(f"{hero.name} enters the arena with {hero.health} health!")
    damage, critical_hit = hero.attack()
    goblin.take_damage(damage, critical_hit)

    damage = goblin.attack()
    hero.take_damage(damage)
    
    



if __name__ == "__main__":
    main()
