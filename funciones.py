import random

turn_counter = 1

def damage_(min_val, max_val):
    damage = random.randint(min_val, max_val)
    if random.randint(1, 10) == 1:
        damage *= 2
    return damage

def status(hero, hp_h, hp_h_max, enemy, hp_e, hp_e_max, potions):
    print("\n" + "="*40)
    print(f"🧪 Potions: {potions}")
    
    hero_blocks = int((hp_h / hp_h_max) * 10)
    print(f"{hero}: [{'#'*hero_blocks}{'-'*(10-hero_blocks)}] {hp_h}/{hp_h_max}")

    enemy_blocks = int((hp_e / hp_e_max) * 10)
    print(f"{enemy}: [{'#'*enemy_blocks}{'-'*(10-enemy_blocks)}] {hp_e}/{hp_e_max}")
    print("="*40)

def winner(hp_h, hp_e):
    return hp_h <= 0 or hp_e <= 0

def enemy_turn(hp_h):
    print("\n👾 ENEMY TURN")
    damage = damage_(15, 20)
    hp_h = max(0, hp_h - damage)
    print(f"The enemy attacks for {damage} damage!")
    return hp_h - damage

def hero_turn(hp_h, hp_e, potions, hp_h_max):
    global turn_counter
    print(f"\n🔥 TURN {turn_counter}")
    print("-"*30)

    while True:
        print("1) ⚔️ Attack")
        print("2) ❤️ Heal")
        print("3) 💥 Special ability")

        option = input("Choose an option: ")

        if option == "1":
            damage = damage_(10, 25)
            print(f"\n⚔️ You dealt {damage} damage!")
            hp_e = max(0, hp_e - damage)
            break

        elif option == "2":
            if potions > 0:
                potions -= 1
                hp_h = min(hp_h_max, hp_h + 20)
                print(f"\n❤️ You healed 20 HP")
                print(f"🧪 Potions left: {potions}")
                break
            else:
                print("\n❌ No potions left!")

        elif option == "3":
            if random.randint(1, 2) == 1:
                damage = damage_(30, 50)
                print(f"\n💥 Critical hit! {damage} damage!")
            hp_e = max(0, hp_e - damage)
        else:
                print("\n❌ Special ability failed!")
        break

    else:
            print("\n⚠️ Invalid option")

    turn_counter += 1
    return hp_e, hp_h, potions