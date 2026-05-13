# finalProject_LongABreauna.py
# 05/12/2026
# Final Project: College Survival Simulator
# This program is a text-based college survival game where the player must survive the semester by balancing energy, stress, GPA, and money. 

import random

import time

# Main character dictionary

student = {

    "name": "",

    "energy": 100,

    "stress": 20,

    "gpa": 3.0,

    "money": 50,

    "week": 1

}

# Inventory dictionary

inventory = {

    "coffee": 2,

    "snacks": 1,

    "study_guides": 0

}

def pause():

    """Pauses the game briefly."""

    time.sleep(1.5)

def show_stats():

    """Displays student stats and inventory."""

    print("\n========== STUDENT STATS ==========")

    print(f"Name: {student['name']}")

    print(f"Week: {student['week']}")

    print(f"Energy: {student['energy']}")

    print(f"Stress: {student['stress']}")

    print(f"GPA: {student['gpa']:.1f}")

    print(f"Money: ${student['money']}")

    print("\nInventory:")

    for item, amount in inventory.items():

        print(f"- {item}: {amount}")

    print("===================================\n")

def study():

    """Player studies for classes."""

    print("\n📚 You spend hours studying...")

    pause()

    student["gpa"] += 0.1

    student["energy"] -= random.randint(10, 20)

    student["stress"] += random.randint(5, 15)

    chance = random.randint(1, 3)

    if chance == 1:

        print("✅ You aced a quiz!")

        student["gpa"] += 0.1

    elif chance == 2:

        print("😵 You pulled an all-nighter.")

        student["energy"] -= 10

    else:

        print("📖 You learned a lot this week.")

    limit_stats()

def sleep_action():

    """Player sleeps to recover."""

    print("\n😴 You get extra sleep...")

    pause()

    student["energy"] += random.randint(20, 35)

    student["stress"] -= random.randint(10, 20)

    print("You feel refreshed!")

    limit_stats()

def work():

    """Player works a job."""

    print("\n💼 You worked a long shift...")

    pause()

    earned = random.randint(20, 60)

    student["money"] += earned

    student["energy"] -= random.randint(10, 20)

    student["stress"] += random.randint(5, 10)

    print(f"You earned ${earned}!")

    limit_stats()

def hang_out():

    """Player hangs out with friends."""

    print("\n🎉 You hang out with friends...")

    pause()

    student["stress"] -= random.randint(15, 25)

    student["energy"] -= random.randint(5, 10)

    outcome = random.randint(1, 2)

    if outcome == 1:

        print("🍕 Free pizza night on campus!")

        student["energy"] += 10

    else:

        print("⚠️ You skipped studying.")

        student["gpa"] -= 0.1

    limit_stats()

def buy_items():

    """Allows player to buy inventory items."""

    print("\n🛒 Campus Store")

    print("1. Coffee ($10)")

    print("2. Snacks ($5)")

    print("3. Study Guide ($20)")

    print("4. Leave Store")

    choice = input("Choose an option: ")

    if choice == "1":

        if student["money"] >= 10:

            student["money"] -= 10

            inventory["coffee"] += 1

            print("☕ Coffee purchased!")

        else:

            print("Not enough money.")

    elif choice == "2":

        if student["money"] >= 5:

            student["money"] -= 5

            inventory["snacks"] += 1

            print("🍫 Snacks purchased!")

        else:

            print("Not enough money.")

    elif choice == "3":

        if student["money"] >= 20:

            student["money"] -= 20

            inventory["study_guides"] += 1

            print("📘 Study guide purchased!")

        else:

            print("Not enough money.")

    elif choice == "4":

        return

    else:

        print("Invalid choice.")

def use_items():

    """Player uses inventory items."""

    print("\n🎒 Inventory")

    print("1. Coffee")

    print("2. Snacks")

    print("3. Study Guide")

    print("4. Back")

    choice = input("Choose an item: ")

    if choice == "1":

        if inventory["coffee"] > 0:

            inventory["coffee"] -= 1

            student["energy"] += 20

            print("☕ You drank coffee and gained energy!")

        else:

            print("No coffee left.")

    elif choice == "2":

        if inventory["snacks"] > 0:

            inventory["snacks"] -= 1

            student["stress"] -= 10

            print("🍫 Snacks helped you relax!")

        else:

            print("No snacks left.")

    elif choice == "3":

        if inventory["study_guides"] > 0:

            inventory["study_guides"] -= 1

            student["gpa"] += 0.2

            print("📘 Study guide improved your GPA!")

        else:

            print("No study guides left.")

    elif choice == "4":

        return

    else:

        print("Invalid choice.")

    limit_stats()

def random_event():

    """Random weekly events."""

    print("\n🎲 Random Event!")

    pause()

    event = random.randint(1, 5)

    if event == 1:

        print("📝 Surprise quiz!")

        student["stress"] += 10

    elif event == 2:

        print("🍕 Free food on campus!")

        student["energy"] += 10

    elif event == 3:

        print("💻 Your laptop crashed.")

        student["stress"] += 15

        student["money"] -= 20

    elif event == 4:

        print("🎉 School event boosted your mood!")

        student["stress"] -= 10

    else:

        print("🏆 Your professor gave extra credit!")

        student["gpa"] += 0.1

    limit_stats()

def limit_stats():

    """Keeps stats within reasonable limits."""

    if student["energy"] > 100:

        student["energy"] = 100

    if student["stress"] < 0:

        student["stress"] = 0

    if student["gpa"] > 4.0:

        student["gpa"] = 4.0

def check_status():

    """Checks win and lose conditions."""

    if student["energy"] <= 0:

        print("\n💀 You completely burned out.")

        print("GAME OVER")

        return False

    elif student["stress"] >= 100:

        print("\n😫 Your stress became overwhelming.")

        print("GAME OVER")

        return False

    elif student["gpa"] < 1.0:

        print("\n📉 Your GPA dropped too low.")

        print("GAME OVER")

        return False

    elif student["week"] > 10:

        print("\n🎓 Congratulations!")

        print("You survived the semester!")

        print("YOU WIN!")

        return False

    return True

def next_week():

    """Moves game to next week."""

    student["week"] += 1

def intro():

    """Introduces the game."""

    print("====================================")

    print("🎓 COLLEGE SURVIVAL SIMULATOR 🎓")

    print("====================================")

    print("Goal: Survive 10 weeks of college")

    print("without failing or burning out!")

    print("====================================\n")

    student["name"] = input("Enter your student name: ")

    print(f"\nWelcome, {student['name']}!")

    pause()

def main():

    """Main game loop."""

    intro()

    playing = True

    while playing:

        print(f"\n📅 WEEK {student['week']}")

        print("\nChoose an action:")

        print("1. Study")

        print("2. Sleep")

        print("3. Work")

        print("4. Hang Out")

        print("5. Buy Items")

        print("6. Use Items")

        print("7. View Stats")

        print("8. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":

            study()

            random_event()

            next_week()

        elif choice == "2":

            sleep_action()

            random_event()

            next_week()

        elif choice == "3":

            work()

            random_event()

            next_week()

        elif choice == "4":

            hang_out()

            random_event()

            next_week()

        elif choice == "5":

            buy_items()

        elif choice == "6":

            use_items()

        elif choice == "7":

            show_stats()

        elif choice == "8":

            print("\nThanks for playing!")

            break

        else:

            print("❌ Invalid choice.")

        playing = check_status()

# Starts the game

main()
