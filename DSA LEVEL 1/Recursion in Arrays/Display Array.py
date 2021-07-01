def prn(n,ar,i):
    if i==n:
        return
    print(ar[i])
    prn(n,ar,i+1)


if __name__ == "__main__":
    n=int(input())
    ar=[]
    for i in range(n):
        ar.append(int(input()))
    prn(n,ar,0)