n=int(input())
arr=[]
count=0
for i in range(n):
    m_arr=list(map(int,input().split()))
    arr.append(m_arr)
for i in range(len(arr)):
    for j in range(len(arr)):
        if i!=j and arr[i][0]==arr[j][1]:
            count+=1
print(count)

