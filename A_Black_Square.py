cal=list(map(int,input().split()))
s=input().strip()
los=0
for i in s:
    strip=int(i)-1
    los+=cal[strip]
print(los)

