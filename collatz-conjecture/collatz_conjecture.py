test = 7

def steps(number):
    presentStep = 0
    n = number

    while n != 1:
        if number > 1:
            # n is even
            if n % 2== 0:
                n = n /2
                presentStep +=1 
            # n is odd:
            else: 
                n = 3*n+1
                presentStep +=1
        else:
            raise ValueError

    print(presentStep)
    return presentStep

steps(test)
