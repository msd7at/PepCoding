def prn(ar,i):
    if i==-1:
        return
    print(ar[i])
    prn(ar,i-1)


if __name__ == "__main__":
    n=int(input())
    ar=[]
    for i in range(n):
        ar.append(int(input()))
    prn(ar,n-1)