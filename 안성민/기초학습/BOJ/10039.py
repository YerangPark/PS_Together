# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())



# if a < 40:
#     a = 40
# if b < 40:
#     b = 40
# if c < 40:
#     c = 40
# if d < 40:
#     d = 40
# if e < 40:
#     e = 40 

# avg = (a+b+c+d+e)/5
# print(int(avg))
sum = 0
for i in range(5):
    N = int(input())
    if N < 40:
        sum += 40
    else:
        sum += N
avg = sum/5
print(sum)
    
    