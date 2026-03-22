# Import all functions and variables from funciones.py
from funciones import *

# --- Initial game state ---
hp_h = 100       # Hero's starting HP
hp_e = 120       # Enemy's starting HP
potions = 3      # Number of healing potions available
hp_h_max = 100   # Hero's maximum HP (used for health bar and healing cap)
hp_e_max = 120   # Enemy's maximum HP (used for health bar)
enemy = "Enemy"  # Enemy display name

# Ask the player for their hero's name
hero_name = input("Enter your hero's name: ")
print(f"\nWelcome, {hero_name}! The battle begins ⚔️")

# --- Main battle loop ---
# Continues until either the hero or enemy reaches 0 HP
while not winner(hp_h, hp_e):

    # Hero takes their turn (attack, heal, or special ability)
    hp_e, hp_h, potions = hero_turn(hp_h, hp_e, potions, hp_h_max)

    # Check if the enemy was defeated after the hero's turn
    if winner(hp_h, hp_e):
        break

    # Enemy takes their turn and damages the hero
    hp_h = enemy_turn(hp_h)

    # Display current HP bars and potion count after each full round
    status(hero_name, hp_h, hp_h_max, enemy, hp_e, hp_e_max, potions)

# --- Battle result ---
if hp_h > 0:
    print("Victory! 🏆")   # Hero survived
else:
    print("Game over... 💀")  # Hero was defeated