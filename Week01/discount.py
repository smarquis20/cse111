"""
Author: Shaun Marquis

Purpose: This program will calculate discounts depending on the day of the week.
"""
from datetime import datetime

#Get users age
user_subtotal = float(input("Please enter your subtotal: "))

#Gets todays date
current_date = datetime.now()

#Get day of week as an integer
day_number = current_date.isoweekday()

#day_number = 5

if (day_number == 2 or day_number == 3) and user_subtotal >= 50:
    discount = user_subtotal * .1
    new_subtotal = user_subtotal - discount
    sales_tax = new_subtotal * .06
    total_due = new_subtotal + sales_tax

    print(f"Discount: ${discount:.2f}")
    print(f"Subtotal: ${new_subtotal:.2f}")
    print(f"Sales Tax: ${sales_tax:.2f}")
    print(f"Total Due: ${total_due:.2f}")

else:
    if (day_number == 2 or day_number == 3) and user_subtotal < 50:
        total_difference = 50 - user_subtotal
        discount = 0
        new_subtotal = user_subtotal - discount
        sales_tax = new_subtotal * .06
        total_due = new_subtotal + sales_tax

        print(f"Subtotal: ${new_subtotal:.2f}")
        print(f"Sales Tax: ${sales_tax:.2f}")
        print(f"Total Due: ${total_due:.2f}")
        print(f"Spend ${total_difference:.2f} more to get the 10% discount.")

    else:
        discount = 0
        new_subtotal = user_subtotal - discount
        sales_tax = new_subtotal * .06
        total_due = new_subtotal + sales_tax

        print(f"Subtotal: ${new_subtotal:.2f}")
        print(f"Sales Tax: ${sales_tax:.2f}")
        print(f"Total Due: ${total_due:.2f}")
