h, m, s = map(int, input().split(':'))
ph, pm, ps = map(int, input().split(':'))

t = (ph*3600 + pm*60 + ps) - (h*3600 + m*60 + s)

if t < 0:
    t += 3600 * 24

h2 = t // 3600
m2 = (t % 3600) // 60
s2 = t % 60

print("%02d:%02d:%02d" % (h2,m2,s2))
