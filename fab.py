def fab(num):
    a = 0
    b = 0
    if num == 0:
       print("Invalid number")
    elif num == 1:
       return a
    else:
       print(a)
       print(b)
       c = a + b
       a = b
       b = c
       print(c)
print(fab(12))    
