import sys
sys.setrecursionlimit(10**6)
def prn(ar,i,x,ans):
    if i==-1:
        return ans
    ab= prn(ar,i-1,x,ans)
    if ar[i]== x:
        ans.append(i)
    return ab



if __name__ == "__main__":
    n=int(input())
    ar=[]
    for i in range(n):  
        ar.append(int(input()))
    x=int(input())
    for f in (prn(ar,n-1,x,[])):
        print(f)
    print()
    