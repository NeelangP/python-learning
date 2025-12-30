import random
import time

def battle_sim():

    player_hp = 100
    enemy_hp = 100
    ult_charge = 0

    print("----Battle Start----")
    print(f"You (HP: {player_hp}) vs. Enemy (HP: {enemy_hp})")
    time.sleep(1)

    while player_hp > 0 and enemy_hp > 0:

        print("\n Your turn")
        print(f"ULT CHARGE: {ult_charge}%")
        print("1. Attack")
        print("2. Heal")
        if ult_charge >= 100:
            print("3. ☄️ ORBITAL STRIKE (READY!)")

        choice = input("Choose action (1/2): ")

        if choice == "1":
            
            crit_chance = random.randint(1, 100)

            if crit_chance <= 15:
                damage =  random.randint(10, 20)*2
                print(f"🎯 HEADSHOT! CRITICAL HIT for {damage} damage!")
            else:
                damage = random.randint(10, 25)
                print(f"💥 You hit the enemy for {damage} damage!")
            enemy_hp -= damage

            if ult_charge < 100:
                ult_charge += 20
                print(f"🔋 Ult Charge: {ult_charge}%")
        
        elif choice == "3":
            damage = 50
            enemy_hp -= damage
            ult_charge = 0
            print(f"☄️ ORBITAL STRIKE HIT FOR {damage} DAMAGE!")

        elif choice == "2":

            heal = random.randint(5 , 10)
            player_hp = player_hp + heal
            print(f"💚 You healed yourself for {heal} HP.")

        else:
            print("Missed turn! (Invalid Input)")

        if enemy_hp <= 0:
            break

        time.sleep(1)
        enemy_miss = random.randint(1, 100)
        if enemy_miss <= 10:
            print("Player dodged the attack")
        else:
            enemy_damage = random.randint(5, 20)
            print(f"⚔️ Enemy attacks you for {enemy_damage} damage!")
            player_hp -= enemy_damage

        print(f"Stats -> You: {player_hp} | Enemy: {enemy_hp}")
        time.sleep(1)

    print("\n Game over")
    if player_hp > 0 :
        print("You Won")
    else:
        print("💀 You died")

battle_sim()