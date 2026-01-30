s=list(input().strip())
u,l=0,0
for i in s:
    if ord(i) >=97:
        l+=1
    else:
        u+=1
if l>=u:
    print(''.join(s).lower())
else:
    print(''.join(s).upper())


