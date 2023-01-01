# def pzn(N):
#     if N % 2 == 0:
#         return 0
#     elif N % 2 == 1:
#         return 1

# N = int(input())
# if pzn(N) == 0:
#     print("짝수")
# elif pzn(N) == 1:
#     print("홀수")

#=================================================


# def fadd(n, m):
#     s = n + m
#     print(n, '+', m, '=', s)

# def fsub(n, m):
#     s = n - m
#     print(n, '-', m, '=', s)

# def fmul(n, m):
#     s = n * m
#     print(n, '*', m, '=', s)

# def fdiv(n, m):
#     s = n / m
#     print(n, '/', m, '=', s)    

# n = int(input())
# m = int(input())
# s = input()
# if s == '+':
#     fadd(n,m)
# elif s == '-':
#     fsub(n,m)
# elif s == '*':
#     fmul(n,m)
# elif s == '/':
#     fdiv(n,m)

#=================================================

# def fadd(n, m):
#     s = n + m
#     return s

# def fsub(n, m):
#     s = n - m
#     return s

# def fmul(n, m):
#     s = n * m
#     return s

# def fdiv(n, m):
#     s = n / m
#     return s  

# n = int(input())
# m = int(input())
# s = input()

# if s == '+':
#     print(n, '+', m, '=',fadd(n,m))

# elif s == '-':
#     print(n, '-', m, '=', fsub(n,m))

# elif s == '*':
#     print(n, '*', m, '=', fmul(n,m))
    
# elif s == '/':
#     print(n, '/', m, '=', fdiv(n,m))
    

#================================================================

import turtle as t

def Triangle_draw():
    t.shape("turtle")
    for i in range(3):
        t.forward(100)
        t.left(120)

def Triangle_area(c,d):
    area = c * d // 2
    return area

b, h = map(int , input().split())
Triangle_draw()
print(Triangle_area(b,h))


