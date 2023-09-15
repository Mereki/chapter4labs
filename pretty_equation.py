# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Caleb Mandapat
#               Mason McIntosh
#               Diego Arroyo
#               Lisandro Demagistris
# Section:      509
# Assignment:   4.14
# Date:         15 September 2023

# Get coefficients
co_A = int(input("Please enter the coefficient A: "))
co_B = int(input("Please enter the coefficient B: "))
co_C = int(input("Please enter the coefficient C: "))

equation = ""

# A checker
if co_A != 0:
    if co_A == 1:
        equation += f'x^2'
    elif co_A == -1:
        equation += f'- x^2'
    elif co_A > 1:
        equation += f'{co_A}x^2'
    elif co_A < 1:
        equation += f'- {abs(co_A)}x^2'

# B checker
if co_B != 0:
    if co_A == 0 and co_B > 1:
        equation += f'{co_B}x'
    elif co_A == 0 and co_B == 1:
        equation += f'x'
    elif co_B == 1:
        equation += f' + x'
    elif co_B > 1:
        equation += f' + {co_B}x'
    elif co_B == -1:
        equation += f' - x'
    elif co_B < 1:
        equation += f' - {abs(co_B)}x'

# C checker
if co_C != 0:
    if co_C > 1:
        equation += f' + {co_C}'
    elif co_C < 1:
        equation += f' - {abs(co_C)}'
    elif co_C == 1:
        equation += f' + {co_C}'

# All together
print(f'The quadratic equation is {equation} = 0')

