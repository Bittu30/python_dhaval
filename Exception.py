# this is Exception handling tutorial

x = input("Enter number 1:")

y = input("Enter number 2:")

try:
    z = int(x) / int(y)
    a = 'baby yoda' + 56
except ZeroDivisionError as ze:
    print('Exception Occured:', ze)
    z = 0
except TypeError as te:
    print('Exception Occured:', te)
    z = 0
except Exception as e:
    print('Generic Exception Occured:', e)
    z = 0

print("division is:", z)
