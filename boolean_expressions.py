############ Part A ############
boolA = input("Enter True or False for a: ")
boolB = input("Enter True or False for b: ")
boolC = input("Enter True or False for c: ")

a = False
b = False
c = False

if boolA == 'T' or boolA == 't' or boolA == 'True':
    a = True
elif boolA == 'F' or boolA == 'f' or boolA == 'False':
    a = False

if boolB == 'T' or boolB == 't' or boolB == 'True':
    b = True
elif boolB == 'F' or boolB == 'f' or boolB == 'False':
    b = False

if boolC == 'T' or boolC == 't' or boolC == 'True':
    c = True
elif boolC == 'F' or boolC == 'f' or boolC == 'False':
    c = False

############ Part B ############

print(f'a and b and c: {a and b and c} ')
print(f'a or b or c: {a or b or c}')

############ Part C ############

XOR = (a and not b) or (not a and b)
print(f'XOR: {XOR}')

odd = a and (not b or c) and (b or not c)
print(f'Odd number: {odd}')

