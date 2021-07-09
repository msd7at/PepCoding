import sys
sys.setrecursionlimit(10**6)
def prn(s):
    if s=="":
        return [""]
    f=s[0] 
    res=s[1:]
    ans=prn(res)

    for i in res:
        ans.append(""+i)
        ans.append(f+i)
    return ans



if __name__ == "__main__":
   s=input()
   a=prn(s)
#    a.append(s)
   print(*a)