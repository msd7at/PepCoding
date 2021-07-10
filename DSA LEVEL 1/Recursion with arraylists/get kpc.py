import sys
sys.setrecursionlimit(10**6)
def prn(s,d):
    if s=="":
        return [""]
    f=s[0] 
    res=s[1:]
    ans=prn(res,d)
    ch=d[f]
    m=[]
    for i in ch:
        for j in ans:
            m.append(i+j)
    return m







if __name__ == "__main__":
   s=input()
   d={"0":".;","1":"abc","2":"def","3":"ghi","4":"jkl","5":"mno","6":"pqrs","7":"tu","8":"vwx","9":"yz"}
   a=prn(s,d)
#    a.append(s)
   print(a)