
# importing the sys module
import sys
 
# the setrecursionlimit function is
# used to modify the default recursion
# limit set by python. Using this,
# we can increase the recursion limit
# to satisfy our needs
 
sys.setrecursionlimit(10**6)
def prn(ar,i):
    if i==len(ar)-1:
        return ar[i]
    # print(m)  
    m=prn(ar,i+1)
    if (m>ar[i]):
        return m
    return ar[i]



if __name__ == "__main__":
    n=int(input())
    ar=[]
    for i in range(n):
        ar.append(int(input()))
    h=prn(ar,0)
    print(h)