t=int(input())
q=int(input())
ans=[0]*t
# for w in range(q):
#     a,b,c=map(int,input().split())
#     for i in range(a,b+1):
#         ans[i]+=c
# print(*ans)
for w in range(q):
    a,b,c=map(int,input().split())
    ans[a]+=c
    if b+1 < t:
        ans[b+1]-=c
s=0
for i in range(len(ans)):
    s+=ans[i]
    ans[i]=s
print(*ans)
