# This program should calculate the pay of an employee based on hours worked.
# The input includes the employee’s total hours worked per week and their hourly pay rate.
# The employee will be paid a base wage for the first 40 hours worked and time-and-a-half (150% of base pay) for any hours past 40 as overtime pay.
# Output the regular pay, overtime pay, and total pay for the week on the screen.
# If the employee worked 40 hours or less, don’t show any output regarding overtime pay.

total_hours_worked = int(input("How many hours worked: "))
hourly_rate = int(input("How much per hours: "))


if(total_hours_worked <= 40):
    regular_pay = total_hours_worked * hourly_rate
    print("Regular Pay:", regular_pay)
else:
    regular_pay = 40 * hourly_rate
    print("Regular Pay:", regular_pay)
    overtime_pay = int((total_hours_worked - 40) * (hourly_rate * 1.5))
    print("Overtime Pay:", overtime_pay)
    print("Total Pay:", regular_pay + overtime_pay)


