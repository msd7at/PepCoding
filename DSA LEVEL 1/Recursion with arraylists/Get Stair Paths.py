import sys
sys.setrecursionlimit(10**6)
# def prn(i,s,c,a):
#     if s==i:
#         a.append(int(c))
#         # print(a)
#         return 
#     elif i>s:
#         return a
#     prn(i+1,s,c+"1",a)
#     prn(i+2,s,c+"2",a)
#     prn(i+3,s,c+"3",a)
#     return a

def prn(s):
    if s==0:
        return [""]
    elif s<0:
        return []
    p1=prn(s-1)
    p2=prn(s-2)
    p3=prn(s-3)
    ans=[]
    for i in p1:
        ans.append("1"+i)
    for i in p2:
        ans.append("2"+i)
    for i in p3:
        ans.append("3"+i)
    return ans


if __name__ == "__main__":
    s=int(input())
    print(prn(s))
#    print(prn(0,s,"",[]))
#    print(a)