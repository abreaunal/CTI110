# A'Breauna Long
# 4/11/2026
# P2HW1: Travel Budget Calculator
# This program takes travel budget, destination, and expenses and displays a formatted summary 




# Ask user for input
budget = float (input("Enter your total budget : $"))
destination = input("Enter your travel destination: ")
gas = float(input("Enter how much you will spend on gas: $"))
accomodation = float(input("Enter how much you will spend on accomodation: "))
food = float(input("Enter how much you will spend on food: $"))

# Calculate total expenses
total_expenses = gas + accomodation+ food

# Calculate remaining budget
remainding_budget = budget - total_expenses 

# ==============FORMATTED OUTPUT=================

print("\n-------- Travel Expense Summary --------\n")

print(f'Destination: {destination:<20}')

print(f'{"Budget:":<20} ${budget:,.2f}')
print(f"{'Gas:':<20} ${gas:,.2f}")
print(f"{'Accommodation:':<20} ${accomodation:,.2f}")
print(f"{'Food:':<20} ${food:,.2f}")

print("--------------------------------------")


print(f'{"Total Expenses:":<20} ${total_expenses:,.2f}')
print(f'{"Remaining Budget:":<20} ${remainding_budget:,.2f}')