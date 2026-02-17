import math
y,w=map(int,input().split())
m=max(y,w)
fav=6-m+1
den=6
g=math.gcd(fav,den)
print(f"{fav//g}/{den//g}")
