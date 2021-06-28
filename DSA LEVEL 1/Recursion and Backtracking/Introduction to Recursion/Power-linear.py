def pow(x,n):
    if n==0:
        return 1
    return x * pow(x,n-1)

if __name__ == "__main__":
    x=int(input())
    n=int(input())
    print(pow(x,n))