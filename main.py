import random
player_hp = 100
monster_hp = 100
while player_hp > 0 and monster_hp > 0:
    print("""1. Attack
2. Heal
3. Run""")
    choice = input("Enter a choice: ").lower()
    if choice == "attack":
        attack = random.randint(10, 25)
        critical_hit = random.randint(1, 10)
        if critical_hit == 5:
            attack *= 2
            print("CRITICAL HIT!")
        print("You hit monster for", attack, "damage")
        monster_hp -= attack
        print(f"Player HP:", player_hp, "Monster HP:", monster_hp)
        if monster_hp <= 0:
            print("Monster defeated!")
            break
        elif monster_hp < 30:
            attack = random.randint(10, 30)
        else:
            attack = random.randint(5, 20)
        print("Monster hits you for", attack, "damage")
        player_hp -= attack
        if player_hp <= 0:
            print("Game over")
            print(f"Player HP:", player_hp, "Monster HP:", monster_hp)
            break
        print(f"Player HP:", player_hp, "Monster HP:", monster_hp)
    elif choice == "heal":
        heal = random.randint(15, 30)
        old_hp = player_hp
        player_hp += heal
        if player_hp > 100:
            player_hp = 100
        real_hp = player_hp - old_hp
        print(f"You healed for", real_hp, "HP")
        attack = random.randint(5, 20)
        print("Monster hits you for", attack, "damage")
        player_hp -= attack
        if player_hp <= 0:
            print("Game over")
            print(f"Player HP:", player_hp, "Monster HP:", monster_hp)
            break
        print(f"Player HP:", player_hp, "Monster HP:", monster_hp)
    elif choice == "run":
        print("You ran away!")
        print(f"Player HP:", player_hp, "Monster HP:", monster_hp)
        break
    else:
        print("Invalid choice")
