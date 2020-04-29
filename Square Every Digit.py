a = ''
def square_digits(num):
    a = ''
    for x in str(num):
        b = int(x)**2
        a = str(a)+str(b)
        a = int(a)
    return a
print(a)    
print(square_digits(9119))