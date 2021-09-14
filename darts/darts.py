def score(x, y):
    def squared(num):
        return num ** 2
    if  squared(x) + squared(y) > 100:
        return 0 
    elif  (squared(x) + squared(y) <= 100) and (squared(x) + squared(y) > 25):
        return 1
    elif  (squared(x) + squared(y) <= 25) and (squared(x) + squared(y) > 1):
        return 5
    elif  squared(x) + squared(y) <= 1:
        return 10



