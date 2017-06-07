def spam(dBy):
    try:
        return 42 / dBy
    except ZeroDivisionError:
        print ('ERROR: Invaild number you cannot divide by zero')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
