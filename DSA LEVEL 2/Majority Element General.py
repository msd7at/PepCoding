n=int(input())
ar=list(map(int,input().split()))
k=int(input())
d={}
for i in ar:
    if i not in d:
        d[i]=0
    d[i]+=1
ans=[]
for i in d:
    if d[i] > n//k:
        ans.append(i)
ans.sort()
print(ans)
