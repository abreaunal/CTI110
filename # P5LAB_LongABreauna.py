# PSLAB_LongABreauna.py
# 05/10/2026
# P5LAB 
# This program stimunlates a self checkout machine by generating a random total owed, accepting payment from the user, calculating change owed, and displaying the change.

import random

# Function to calculate and display change
def disperse_change(change):

# Convert change to pennies
    change = round(change * 100)
    
    dollars = change // 100
    change = change % 100

    quarters = change // 25
    change = change % 25

    dimes = change // 10
    change = change % 10

    nickels = change // 5
    change = change % 5

    pennies = change

    print("\nChange is:")
    if dollars > 0:
        print(dollars, "Dollar(s)")

    if quarters > 0:
        print(quarters, "Quarter(s)")
        
    if dimes > 0:
        print(dimes, "Dime(s)")

    if nickels > 0:
        print(nickels, "Nickel(s)")

    if pennies > 0:
        print(pennies, "Pennie(s)")

# Main Function
def main():
    
    # Generate random total owed
    total_owed = round(random.uniform(0.01, 100.00), 2)

    print(f"You owe: ${total_owed}")

    # Get money from customer
    cash = float(input("How much cash will you put in the self-checkout? "))


    # Calculate change
    change_owed = cash - total_owed

    print(f"Change owed: ${change_owed:.2f}")

    # Call function
    disperse_change(change_owed)

# Call main function
main()

