import turtle as t

def Triangle_draw():
    t.shape("turtle")
    for i in range(3):
        t. forward(100)
        t. left(120)

def Triangle_area(n, m):
    area = (n*m)/2
    return area

n, m = map(int, input().split())
Triangle_draw()
print(Triangle_area(n,m))

