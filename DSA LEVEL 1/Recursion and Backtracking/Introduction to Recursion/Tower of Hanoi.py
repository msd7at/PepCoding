def toh(n,a,b,c):
    if(n==0):
        return 
    toh(n-1,a,c,b)
    print("{}[{} -> {}]".format(n,a,b))
    toh(n-1,c,b,a)


if __name__ == "__main__":
    n=int(input())
    a=int(input())
    b=int(input())
    c=int(input())
    toh(n,a,b,c)