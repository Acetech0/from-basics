def a (x, y):
    if y == 0:
        return x
    else:
        return a (x+1 , y-1)
b = 10
c = 25
d = a(b ,c)
print(f"sum of {b} and {c} is {d}")