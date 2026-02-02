w=int(input())
for i in range(w):
    n,k,d=map(int,input().split())
    arr=list(map(int,input().split()))
    m_len=float('inf')
    k=0
    j=(k+d)
    while j<=n:
        m_set=len(set(arr[k:j]))
        m_len=min(m_len,m_set)
        k+=1
        j+=1
    print(m_len)


