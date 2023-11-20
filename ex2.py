import math
number = float(input("enter a float"))
if number < 0:
    print("Error, root of negative number do not exist")
else:
    root = math.sqrt(number)
    print('{:.3f}'.format(root))
word1 = input("first word")
word2 = input(' second word')
if len(word1) < len(word2):
    print(word1+' is smaller')
if len(word1) < len(word2):
    print('word are equal')
else:
    print(word2+' is smaller')
    print('now using the ternary operation')
small = word1 if len(word1) < len(word2) else word2
print('the small is ' + small)
# 3 start here
pseuil = 2.3
vseuil = 7.41
tvolume = float(input('enter tidal volume '))
pressure = float(input('enter pressure '))
if pressure > pseuil and tvolume > vseuil:
    print('stop immediately')
elif pressure > pseuil:
    print('increase the volume of the enclosure')
elif tvolume > vseuil:
    print('reduce speaker volume')
else:
    print('everything is okay')