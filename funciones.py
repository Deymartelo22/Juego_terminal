import random

# Global turn counter to track the current turn number
turn_counter = 1

def damage_(min_val, max_val):
    """Calculate random damage, with a 10% chance of dealing double damage (critical hit)."""
    damage = random.randint(min_val, max_val)
    # 1 in 10 chance of critical hit (double damage)
    if random.randint(1, 10) == 1:
        damage *= 2
        print("🎯 Critical hit! Double damage!")
    return damage

def status(hero, hp_h, hp_h_max, enemy, hp_e, hp_e_max, potions):
    """Display the current battle status with health bars for both characters."""
    print("\n" + "="*40)
    print(f"🧪 Potions: {potions}")

    # Build hero health bar (10 blocks total)
    hero_blocks = int((hp_h / hp_h_max) * 10)
    print(f"{hero}: [{'#'*hero_blocks}{'-'*(10-hero_blocks)}] {hp_h}/{hp_h_max}")

    # Build enemy health bar (10 blocks total)
    enemy_blocks = int((hp_e / hp_e_max) * 10)
    print(f"{enemy}: [{'#'*enemy_blocks}{'-'*(10-enemy_blocks)}] {hp_e}/{hp_e_max}")
    print("="*40)

def winner(hp_h, hp_e):
    """Return True if either the hero or enemy has 0 or less HP."""
    return hp_h <= 0 or hp_e <= 0

def enemy_turn(hp_h):
    """Handle the enemy's attack turn and return the hero's updated HP."""
    print("\n👾 ENEMY TURN")

    # Enemy deals between 15 and 20 damage
    damage = damage_(15, 20)

    # Subtract damage but never go below 0
    hp_h = max(0, hp_h - damage)
    print(f"The enemy attacks for {damage} damage!")

    # Return the already-calculated HP (not subtract again)
    return hp_h

def hero_turn(hp_h, hp_e, potions, hp_h_max):
    """Handle the hero's turn: attack, heal, or use special ability."""
    global turn_counter

    print(f"\n🔥 TURN {turn_counter}")
    print("-"*30)

    # Keep asking until the player makes a valid action
    while True:
        # Show available options
        print("1) ⚔️  Attack")
        print("2) ❤️  Heal")
        print("3) 💥 Special ability")
        option = input("Choose an option: ")

        if option == "1":
            # Normal attack: deals 10 to 25 damage
            damage = damage_(10, 25)
            print(f"\n⚔️ You dealt {damage} damage!")
            hp_e = max(0, hp_e - damage)
            break  # Valid action chosen, exit loop

        elif option == "2":
            if potions > 0:
                # Use a potion to heal 20 HP (cannot exceed max HP)
                potions -= 1
                hp_h = min(hp_h_max, hp_h + 20)
                print(f"\n❤️ You healed 20 HP")
                print(f"🧪 Potions left: {potions}")
                break  # Valid action chosen, exit loop
            else:
                # No potions available, ask again
                print("\n❌ No potions left!")

        elif option == "3":
            # Special ability: 50% chance of success
            if random.randint(1, 2) == 1:
                # Success: deals 30 to 50 damage
                damage = damage_(30, 50)
                print(f"\n💥 Special ability hit! {damage} damage!")
                hp_e = max(0, hp_e - damage)  # ✅ solo resta si tuvo éxito
            else:
                # Failure: no damage dealt
                print("\n❌ Special ability failed!")
            break  # ✅ el turno termina siempre, sin importar el resultado

        else:
            # Invalid input, prompt the player again
            print("\n⚠️ Invalid option, please choose 1, 2 or 3.")

    # Increment turn counter after each hero action
    turn_counter += 1
    return hp_e, hp_h, potions