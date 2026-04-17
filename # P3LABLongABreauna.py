# P3LABLongABreauna 
# ABreauna Long
# 04/16/2026
# This program takes a monetary amount as input and calculates the most efficient number of dollars, quarters, dimes, nickles, and pennies needed to make that amount.

# Get user input
amount = float(input("Enter the amount of money:"))

# Convert to cents (integer)
cents = int(amount * 100)

# Calculate Dollars
Dollars = cents // 100
cents = cents - (Dollars * 100)

# Calculate quarters
quarters = cents // 25
cents = cents - (quarters * 25)

# Calculate dimes
dimes = cents // 10
cents = cents - (dimes * 10)

# Calculate nickeles 
nickels = cents // 5
cents = cents - (nickels * 5)

# Remaining cents are pennies 
pennies = cents 

# Display results
if Dollars == 0 and quarters == 0 and dimes == 0 and nickles == 0 and pennies == 0:
    print("No Change")
else:
 if Dollars > 0:
    if Dollars == 1:
        print("1 Dollar")
    else:
        print (Dollars, "Dollars")
    
 if quarters > 0:
    if quarters == 1:
        print("1 quarter")
    else:
        print(quarters, "quarters")

 if dimes > 0:
    if dimes == 1:
        print("1 dime")
    else:
        print(dimes, "dimes")

 if nickels > 0:
    if nickels == 1:
        print("1 nickle")
    else:
        print(nickles, "nickels") 

 if pennies > 0:
    if pennies == 1:
        print("1 penny")
    else:
        print(pennies,"pennies") 
