n=int(input())
l=list(map(int,input().split()))
m=l[0]
le=len(l)
m=l[-1]
right=[0]*le
right[-1]=l[-1]
for i in range(le-2,-1,-1):
    m*=l[i]
    right[i]=m
an=1
for i in range(le-1):
    right[i]=an* right[i+1]
    an=an*l[i]
right[-1]=an
# print(right)
print(*right)
