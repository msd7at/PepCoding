n=int(input())
ar=[]
for i in range(n):
    ar.append(int(input()))
i=0
j=n-1
globalMax=0
m=0
while i<j:
    a=(j-i)*min(ar[j],ar[i])
    globalMax=max(globalMax,a)
    if ar[i]<ar[j]:
        i+=1
    else:
        j-=1
print(globalMax)
    
