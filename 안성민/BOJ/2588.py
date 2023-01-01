a = int(input())
b = int(input())

import math
print((b%10) * a)
print(((math.floor(b/10)))%10*a)
print((math.floor(b/100))*a)
print(a * b)
