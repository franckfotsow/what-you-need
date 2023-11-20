import math
for numb in range(-3,4):
    try:
        print(math.sin(numb)/numb)
    except ZeroDivisionError:
        print("cannot be divided by zero")
