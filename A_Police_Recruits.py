n=int(input())
arr=list(map(int,input().split()))
untreated=0
available=0
for i in arr:
    if i==-1:
        if available>0:
            available-=1
        else:
            untreated+=1
    else:
         available+=i

print(untreated)

        





