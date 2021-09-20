c=int(input())
ar=list(map(int,input().split()))
na=[0]*len(ar)
i=0
j=len(ar)-1
x=-1
while i<j:
    if j-i==1:
        na[0]=min(abs(ar[i]),abs(ar[j]))**2
        na[1]=max(abs(ar[i]),abs(ar[j]))**2
        break
    else:
        if abs(ar[i])<abs(ar[j]):
            na[x]=abs(ar[j])**2
            j-=1
        else:
            na[x]=abs(ar[i])**2
            i+=1
        x-=1
print(*na)
