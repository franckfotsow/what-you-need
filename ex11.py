import math
def cube(numb):
    return numb ** 3
def volumespere(raduis):
    volume=4/3 * math.pi * cube(raduis)
if __name__=='__main__':
    volumespere(2)