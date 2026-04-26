# P4HW2_LongABreauna.py 
# 04/26/2026
# P4HW2
# This program calculates gross pay (including overtime) for multiple employees.
# It keeps running totals for overtime pay, regular pay, gross pay, and employee count.
# The program stops only when the user enters "Done" as the employee name.

# --------------- INITIAL TOTALS ----------------- #
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0 
employee_count = 0

# -------------- FIRST INPUT -------------- #
employee_name = input('Enter employee\'s name or "Done" to terminate: ')

# -------------- LOOP -------------- #
while employee_name != "Done":
    
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
    
    # overtime calculation
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * pay_rate * 1.5
        regular_pay = 40 * pay_rate
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours_worked * pay_rate

    gross_pay = regular_pay + overtime_pay

    # ----------- INDIVIDUAL OUTPUT ----------- #
    print(f"\nEmployee name: {employee_name}")
    print("Hours Worked")
    print("Pay Rate")
    print("OverTime")
    print("OverTime Pay")
    print(f"{hours_worked:.1f}")
    print(f"{pay_rate:.2f}")
    print(f"{overtime_hours:.1f}")
    print(f"{overtime_pay:.2f}")

    print(f"RegHour Pay\n$ {regular_pay:.2f}")
    print(f"Gross Pay\n$ {gross_pay:.2f}\n")

    # ----------- TOTALS UPDATE ----------- #
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    # next employee
    employee_name = input('Enter employee\'s name or "Done" to terminate: ')

# ---------- FINAL SUMMARY ---------- #
print(f"\nTotal number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")