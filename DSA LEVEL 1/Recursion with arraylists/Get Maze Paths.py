import sys
sys.setrecursionlimit(10**6)
def prn(i,j,n,m):
    if i==n-1 and j==m-1:
        return [""]
    h=[]
    v=[]
    
    if i<n:
        h= prn(i+1,j,n,m)
    if j<m:
        v=prn(i,j+1,n,m)
    path=[]
    for i in h:
        path.append("h"+i)
        print(path)
    for i in v:
        path.append("v"+i)
        print(path)
    return path



if __name__ == "__main__":
    n=int(input())
    m=int(input())
    q=prn(0,0,n,m)
    print(q)


