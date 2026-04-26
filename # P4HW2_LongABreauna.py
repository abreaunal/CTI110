# P4HW2_LongABreauna.py 
# 04/26/2026
# P4HW2
# This program calculates gross pay (including overtime) for multiple employees. It keeps running totals for overtime pay, reguar pay, gross pay, and employee count.The program stops only when the user enters "Done" as the employee name.

"""
PSEUDOCODE: 

START 
Initialize total_overtime_pay = 0
Initialize total_regular_pay = 0
Initialize total_gross_pay = 0 
Initialize employee_count = 0

Ask the employee name 

WHILE employee name is NOT "Done"
Ask for pay rate
Ask for hours worked

IF hours worked > 40 
calculate overtime hours
calculate overtime pay (hours over 40 * pay rate * 1.5)

ELSE
overtime pay = 0
regular pay = hours worked * pay rate

calculate gross pay = regular pay + overtime pay

add overtime pay to total_overtime_pay
add regular pay to total_regular_pay
add gross pay to total_gross_pay
increase employee_count by 1    

Ask for the next employee name (or "Done")
END
"""

# -------------PROGRAM START-------------- #

total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

employee_name = input("Enter employee name (or 'Done' to terminate): ")

while employee_name != "Done":

    pay_rate = float(input("Enter pay rate: "))
    hours_worked = float(input("Enter hours worked: "))

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * pay_rate * 1.5
        regular_pay = 40 * pay_rate
    else:
        overtime_pay = 0
        regular_pay = hours_worked * pay_rate

    gross_pay = regular_pay + overtime_pay

    print("\n--- Employee Pay Details ---")
    print(f"Employee: {employee_name}")
    print(f"Regular Pay: ${regular_pay:.2f}")
    print(f"Overtime Pay: ${overtime_pay:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}\n")

total_overtime_pay += overtime_pay
total_regular_pay += regular_pay
total_gross_pay += gross_pay
employee_count += 1
        
employee_name = input("Enter employee name (or 'Done' to terminate): ")

# Final Results 
print("\n======= FinalSummary =======")
print(f"Total Employees Processed: {employee_count}")
print(f"Total Regular Pay: ${total_regular_pay:.2f}")
print(f"Total Overtime Pay: ${total_overtime_pay:.2f}")
print(f"Total Gross Pay: ${total_gross_pay:.2f}")