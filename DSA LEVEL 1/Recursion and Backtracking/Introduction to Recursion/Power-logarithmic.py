def pow(x,n):
    if n==0:
        return 1
    elif n==1:
        return x
    t=pow(x,n//2)
    if n%2:
        return x * t * t  
    return t*t

if __name__ == "__main__":
    x=int(input())
    n=int(input())
    print(pow(x,n))