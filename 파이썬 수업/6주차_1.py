# id = "성결대학교"
# pw = "파이데이아1"

# for i in range(10):
#     loginid = input("새 아이디 : ")
#     loginpw = input("새 비번 : ")
#     if loginid == id and loginpw == pw:
#         print("접속을 환영합니다")
#         break
#     else:
#         print("아이디와 비번을 정확히 입력하세요")

# number = [0, 0, 0, 0 ,0]
# for i in range(5):
#     number[i] = int(input())
# print(number)

# list1 = [1, 2, 3, 4, 5]
# s = 0

# for i in list1:
#     s += 1
#     print("s :", s)

# N = int(input())
# for i in range(1, 10):
#     print(f"{N} * {i} = {N*i} ",end="")

xxl = 0
xl = 0
m = 0
s = 0
xs = 0

Size = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    Size[i] = int(input("치수를 입력하시오 : "))
    if Size[i] >= 100:
        xxl += 1 
    elif Size[i] >= 95:
        xl += 1
    elif Size[i] >= 90:
        m += 1
    elif Size[i] >= 85:
        s += 1
    else:
        xs += 1
print(xxl, xl, m, s, xs)
print(Size)