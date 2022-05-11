# Gross bonus entries
from __future__ import print_function
from multiprocessing.sharedctypes import Value


gb1 = int(input("Bonus #1 Gross: $"))
gb2 = int(input("Bonus #2 Gross: $"))
gb3 = int(input("Bonus #3 Gross: $"))
gb4 = int(input("Bonus #4 Gross: $"))
gb5 = int(input("Bonus #5 Gross: $"))

# Net bonus entries
nb1 = int(input("Bonus #1 Net: $"))
nb2 = int(input("Bonus #2 Net: $"))
nb3 = int(input("Bonus #3 Net: $"))
nb4 = int(input("Bonus #4 Net: $"))
nb5 = int(input("Bonus #5 Net: $"))

# Need a prompt to ask 'are there more bonuses to enter?'
# Need to calc net amounts

bonus_total = bon1 + bon2 + bon3 + bon4 + bon5

print("You've grossed $",bonus_total, "in bonuses this year.")

# Ultimately want this program to give me an average of the tax rate I am paying
print("Average tax rate on bonuses: ")

print("test")