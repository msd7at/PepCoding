n=int(input())
l=list(map(int,input().split()))
left=[l[0]]
m=l[0]
le=len(l)
for i in range(1,le):
    m*=l[i]
    left.append(m)
m=l[-1]
right=[0]*le
right[-1]=l[-1]
for i in range(le-2,-1,-1):
    m*=l[i]
    right[i]=m
ans=[]
for i in range(le):
    if i-1 >=0:
        ll=left[i-1]
    else:
        ll=1
    if i+1<le:
        rr=right[i+1]
    else:
        rr=1
    ans.append(ll*rr)
print(*ans)
