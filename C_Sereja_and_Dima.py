n=int(input())
card=list(map(int,input().split()))
s_score,d_score,l,r,turn=0,0,0,n-1,0
while l<=r:
    if card[l]>card[r]:
        chosen=card[l]
        l+=1
    else:
        chosen=card[r]
        r-=1
    if turn==0:
        s_score+=chosen
        turn=1
    else :
        d_score+=chosen
        turn=0
print(s_score,d_score)

