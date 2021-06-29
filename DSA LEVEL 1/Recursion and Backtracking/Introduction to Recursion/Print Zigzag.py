def zig(n):
    if n==0:
         
         return
    print(n,end=" ")
    zig(n-1)
    print(n,end=" ")
    zig(n-1)
    print(n,end=" ")
if __name__ == "__main__":
    x=int(input())
    (zig(x))