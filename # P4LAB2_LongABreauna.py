# P4LAB2_LongABreauna
# 04/26/2026
# Program displays multiplication table using a for a loop and repeats a while loop

run_again ="yes"

while run_again=="yes":

    number = int(input("Enter an integer: "))

    if number >= 0:
        for x in range(1, 13):
            print(number, "x", x, "=", number * x)
        else:
            print("This program does not handle negative values.")

            run_again = input("Would you like to run the program again? (yes/no): ").lower()
    
print("Program ended.")