s=input().strip()
current=0
step=0
for i in s:
    target=ord(i)-ord('a')
    diff=abs(current-target)
    step+=min(diff,26-diff)
    current=target
print(step)