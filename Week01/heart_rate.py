"""
Author: Shaun Marquis

Purpose: This program will calculate your heart range depending on your age.
"""
#Get users age
user_age = input("Please enter your age: ")

#Convert user age to an integer
user_age = int(user_age)

max_heart = 0
top_goal = 0
bottom_goal = 0

#Calculate max heart rate according to age
max_heart = 220 - user_age

top_goal = max_heart * .85
bottom_goal = max_heart * .65

print("When you exercise to strengthen your heart, you should")
print(f"keep your heart rate between {bottom_goal:.0f} and {top_goal:.0f} beats per minute.")