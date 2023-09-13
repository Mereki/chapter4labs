# Coin functions
def quarters(x):
    count = 0
    while x >= 0.25:
        x -= 0.25
        count += 1
    return count


def dimes(x):
    count = 0
    while x >= 0.10:
        x -= 0.10
        count += 1
    return count


def nickels(x):
    count = 0
    while x >= 0.05:
        x -= 0.05
        count += 1
    return count


def pennies(x):
    x = round(x, 2)
    count = 0
    while x >= 0.01:
        x -= 0.01
        x = round(x, 2)
        count += 1
    return count


# Get cost and how much user paid
paid = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))

# Change
change = paid - cost
print(f'You received ${change:.2f} in change. That is...')

checker = change

# If / elif statements call functions
if quarters(checker) > 1:
    print(f'{quarters(checker)} quarters')
    checker -= round(quarters(checker) * 0.25, 2)
elif quarters(checker) == 1:
    print(f'{quarters(checker)} quarter')
    checker -= round(quarters(checker) * 0.25, 2)

if dimes(checker) > 1:
    print(f'{dimes(checker)} dimes')
    checker -= round(dimes(checker) * 0.10, 2)
elif dimes(checker) == 1:
    print(f'{dimes(checker)} dime')
    checker -= round(dimes(checker) * 0.10, 2)

if nickels(checker) > 1:
    print(f'{nickels(checker)} nickels')
    checker -= round(nickels(checker) * 0.05, 2)
elif nickels(checker) == 1:
    print(f'{nickels(checker)} nickel')
    checker -= round(nickels(checker) * 0.05, 2)

if pennies(checker) > 1:
    print(f'{pennies(checker)} pennies')
elif pennies(checker) == 1:
    print(f'{pennies(checker)} penny')
