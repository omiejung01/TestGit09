

def hello2():
    a = 5
    print(a)

def hello3():
    print('A')
    print('B')
    print('C')

def cond01():
    a = 330
    b = 200
    if b > a:
        print("b is greater than a")  # This line starts with indent
        print('D')
        print('E')

def cond02():
    a = 200
    b = 33
    if b > a:
        print("b is greater than a")
        print('G')
    else:
        print("b is not greater than a")

def cond03():
    a = 200
    b = 33
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")
    else:
        print("a is greater than b")



