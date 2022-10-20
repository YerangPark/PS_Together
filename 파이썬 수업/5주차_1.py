# score = int(input())

# if score >= 95:
#     print("A+")
# if(score >= 90):
#     print("A")
# if(score >= 85):
#     print("B+")
# if(score >= 80):
#     print("B")
# if(score >= 75):
#     print("C+")
# if(score >= 70):
#     print("C")


# id = int(input())

# if id == 1:
#     print("남자입니다.")
# else:
#     print("여자입니다")

# Temp = int(input())

# if Temp >= 20:
#     print("반팔")
# elif Temp >= 10:
#     print("긴팔")
# else:
#     print("패딩")


xxl = 0
xl = 0
m = 0
s = 0
xs = 0

for i in range(5):
    Size = int(input("치수를 입력하시오 : "))
    if Size > 100:
        xxl += 1 
    elif Size > 95:
        xl += 1
    elif Size > 90:
        m += 1
    elif Size > 85:
        s += 1
    elif Size > 80:
        s += 1
print(xxl, xl, m, s, xs,)



