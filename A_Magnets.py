n=int(input())
prev=input().strip()
groups=1
for i in range(n-1):
    m=input().strip()
    if m != prev:
        groups+=1
    prev=m
print(groups)

# g=[]
# mp,pm=0,0
# for i in range (n):
#     t=input()
#     if t=='10':
#         mp+=1
#         if pm!=0:
#             g.append(pm)
#             pm=0
#     else:
#         pm+=1
#         if mp!=0:
#             g.append(mp)
#             mp=0
# if mp!=0:
#     g.append(mp)
# if pm!=0:
#     g.append(pm)
# print(len(g))
