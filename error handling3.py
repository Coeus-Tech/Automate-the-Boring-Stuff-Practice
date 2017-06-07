def spam(Dby):
    return 42 / Dby
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print ('Error: Invalid argument.')
    
