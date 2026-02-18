s=input().strip()
t=input().strip()
count=1
j,i=0,0
while j<len(t):
    if t[j]==s[i]:
        count+=1
        i+=1
        j+=1
    else:
        j+=1
print(count )