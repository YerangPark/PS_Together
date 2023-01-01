h, b, c, s = map(int, input().split())
sumbit = h*b*c*s

sumbyte = sumbit/8
sumkb = sumbyte/1024
summb = sumkb/1024
print("%0.1f MB" %summb)
