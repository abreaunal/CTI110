# PWHW1_LongABreauna
# 04/24/2026
# PWHW1- Score List with Loop and Grade
# This program collects a user-defined number of scores, validates input,removes the lowest score, calculates the average, and assigns a letter grade.

"""
Psuedocode (Algorithm):

1. Ask user how many scores they want to enter
2. Create an empty list to store scores

3. Loop until the number of scores 
    a. Ask user for a score
    b. While score is not between 0 and 100:
        - Display error message 
        - Ask for score again
    c. Add the score to the list

4. Find the lowest score using min()
5. Remove the lowest score from the list 

6. Calculate:
    - Total using sum()
    - Average = total / count

7. Determine letter grade:
    - 90-100: A
    - 80-89: B
    - 70-79: C
    - 60-69: D
    - Below 60: F

8. Display :
    - Lowest score
    - Average
    - Letter grade
    """

 # Ask for number of scores
from itertools import count


num_scores = int(input("How many scores do you want to enter? "))

scores = []

# Collect scoresusing loop
for i in range(num_scores):
    score = float(input(f"Enter score {i + 1}: "))

    # Validate score
    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score {i + 1}: "))

    scores.append(score)

# Find and remove lowest score
lowest_score = min(scores)
scores.remove(lowest_score)

# Calculate average
total = sum(scores)
average = total / len(scores)

# Determine letter grade
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

# Display results
print("\n------------Results------------")
print(f"Lowest Score: {lowest_score}")
print(f"Modified List : {scores}:")
print(f"Average Score: {average:.2f}")
print(f"Grade  : {grade}")
