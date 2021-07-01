import sys
sys.setrecursionlimit(10**6)
def prn(ar,i,x):
    if i==len(ar):
        return -1
    ab= prn(ar,i+1,x)
    if ar[i]== x:
        return i
    return ab



if __name__ == "__main__":
    n=int(input())
    ar=[]
    for i in range(n):  
        ar.append(int(input()))
    x=int(input())
    print(prn(ar,0,x))
    