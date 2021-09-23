n=input()
n=list(n)

def rev(a,b,ar):
    while a<b:
        ar[a],ar[b]=ar[b],ar[a]
        a+=1
        b-=1

i=len(n)-2
while i>=0 and n[i]>=n[i+1]:
    i-=1
if i == -1:
    print(-1)
else:
    k=len(n)-1
    while k>=0 and n[k]<=n[i]:
        k-=1
    n[k],n[i]=n[i],n[k]
    rev(i+1,len(n)-1,n)
    print("".join(n))
