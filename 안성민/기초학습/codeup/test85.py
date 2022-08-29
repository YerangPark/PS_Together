a,b,c=map(int,input().split())

totalbit=a*b*c
totalbyte=totalbit/8
totalkb=totalbyte/1024
totalmb=totalkb/1024

print("%0.2f MB" % totalmb)