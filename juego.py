#Import functions from another file
from funciones import *

#Character health
hp_h = 100 
hp_e = 120
potions = 3

hero_name = input("Enter your hero's name: ")

hp_h_max = 100
hp_e_max = 120
enemy = "Enemy"

print(f"\nWelcome, {hero_name}! The battle begins ⚔️")

while not winner(hp_h, hp_e):
    hp_e, hp_h, potions = hero_turn(hp_h, hp_e, potions, hp_h_max)

    if winner(hp_h, hp_e):
        break

    hp_h = enemy_turn(hp_h)
    status(hero_name, hp_h, hp_h_max, enemy, hp_e, hp_e_max, potions)

if hp_h > 0:
    print("Victory!")
else:    
    print("Game over...")
