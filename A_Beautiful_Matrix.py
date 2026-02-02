coll=[]
count=0
for i in range(5):
    m_arr=list(map(int,input().split()))
    if 1 in m_arr:
        col=abs(2-m_arr.index(1))
        count+=col
    coll.append(m_arr)
for i in range(5):
    if 1 in coll[i]:
        row=abs(2-i)
        count+=row
print(count)
    