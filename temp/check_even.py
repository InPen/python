number = 7
remainder = number % 2
if remainder == 0:
    print("It's even!")
else:
    print("It's odd!")

# For an even number, print "It's even!"
# For an odd number, print "It's odd!"


# Homework

x = 8
y = 0
a = "Hello!"
b = ""

if x and b:
    print('x and b are true')

if y or a:
    print('one of y or a is false')

if x or y:
    print('one of x or y is false')

if bool(x) == False or bool(y) == False:
    if x > y:
        print('x is greater than y')
