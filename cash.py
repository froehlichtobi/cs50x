from cs50 import get_float

while True:
    change = get_float("Change owed: ")
    if change >= 0:
        break

# the only coins available are quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢)
min_coins = 0

for i in (0.25, 0.10, 0.05, 0.01):
    min_coins += int(change/i)
    # round in order not to have problems with floating point impercision
    change = round(change % i, 5)

print(min_coins)
