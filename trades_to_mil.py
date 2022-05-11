# Ask the user to enter their current balance
# If there is <= $0, tell them they have nothing in the account.  If there is > $0, continue to calculation
# Tell them how many 1% trades it will take to get them to $1m based on their current account balance


balance = int(input("What it your current account balance: "))
counter = 0
goal = 1000000

if balance <= 0:
    print("You have nothing in your account.")
elif balance >= goal:
    print("You have reached your goal, you have $",balance, "dollars in your account.")
else:
    #print("You are getting closer to your goal. Now for the calculation...")
    pass
while balance > 0 and balance <= goal:
    balance = balance * 1.01
    counter = counter + 1
print("Trades to go: ", counter)
