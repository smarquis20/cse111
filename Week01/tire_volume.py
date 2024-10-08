"""
Author: Shaun Marquis

Purpose: This program will calculate the volume of a tire and will save the inputed data to a file called volume.txt
"""
import math
from datetime import datetime

#Get tire measurements from the user
tire_width = int(input("Enter the width of the tire in mm (ex 205): "))
tire_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
wheel_diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

#Set current date/time from local machine and save to a variable
current_dt = datetime.now()

#Calculate tire volume
total_volume = math.pi * math.pow(tire_width, 2) * tire_ratio * (tire_width * tire_ratio + 2540 * wheel_diameter) / 10000000000

print(f"\nThe approximate volume is {total_volume:.2f} liters")

user_purchase = input("Do you want to buy tires with the dimensions entered? (yes/no): ")

if user_purchase.upper() == 'YES':
    user_phone = input("Please enter your phone number (EX. 555-555-5555): ")

    print("Phone number saved. Thank you!")
    #Open file and append tire data and date to volumes.txt
    with open("volumes.txt", "at") as volume_file:

        # Print date, tire information, and user phone number to the volumes.txt file.
        print(f"{current_dt:%Y-%m-%d}, {tire_width}, {tire_ratio}, {wheel_diameter}, {total_volume:.2f}, {user_phone}", file=volume_file)

else:
    print("Thank you have a nice day!")

    #Open file and append tire data and date to volumes.txt
    with open("volumes.txt", "at") as volume_file:

        # Print tire information and date to volumes.txt
        print(f"{current_dt:%Y-%m-%d}, {tire_width}, {tire_ratio}, {wheel_diameter}, {total_volume:.2f}", file=volume_file)