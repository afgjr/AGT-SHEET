a,n=map(int,input().split())
arr=list(map(int,input().split()))
count=0
for i in arr:
    if i <=n:
        count+=1
    else:
        count+=2
print(count)