

def forloop01():
    fruits = ["apple", 100.05 , "banana", "cherry","pineapple"]
    print(len(fruits))

    for x in fruits:
        print('There is the ' + str(x))

def forloop02():
    full_name = 'Assumption university'
    print (len(full_name))

    for x in full_name:
        print ('The alphabet is ' + x)

def forloop03():
    #Do not print a spacebar
    full_name = 'Assumption university'

    for x in full_name:
        if ( x != ' '):
            print ('The alphabet is ' + x)

def whileloop01():
    #Fine sum = 1 + 2 + 3 + 4 +... + 6
    i = 1
    sum = 0
    while i <= 6:
        sum += i
        i += 1 # i = i + 1

    print (sum)


def whileloop02():
    # 10 + 15 + 20 + ... + 195 + 200
    # Start with 10 , increase 5 , end with 200
    i = 10
    sum = 0
    while i <= 200:
        sum += i
        i += 5  # i = i + 5

    print(sum)

def loop_range():
    nums = range(10,205,5) # --> [10,15,20, .... , 200]
    sum = 0
    for x in nums:
        sum += x
        print(x)
    print (sum)

def findMax():
    scores = [5, 8, 7, 3]
    max = 0
    for x in scores:
        if x > max:
            max = x

    print('Maximum value is ', max)

def findMin():
    scores = [5, 8, 7, 3]
    min = 100
    for x in scores:
        if x < min:
            min = x

    print('Minimum value is ', min)


