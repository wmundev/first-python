#!/usr/bin/python

def main():
    print("Hello world")


# check whether this class is run, making it the main program, therefore run the main function.
if __name__ == "__main__":
    main()

f = 6
print(f)

print("wow" + str(123))


def function():
    global f
    f = "def"
    print(f)
    return "wow"


def function1(arg1, arg2):
    print(arg1 + arg2)


def cube(num):
    return num*num*num


def power(num, powerOf):
    for i in range(powerOf):
        num = num * num
    return num


def multiVar(*args):
    for i in args:
        print(i)


multiVar(3,2,1,3,4,5)

x = 4
y = 4
if(x<y):
    print("x is less than y")
elif(x==y):
    print("x is the same as y")
else:
    print("x is more than y")


st = "x is less than y" if(x<y) else "x is more than y"
print(st)

print(power(2,2))


# print(cube(19000))
# function1(1, 2)
#
# function()
# print(function())


