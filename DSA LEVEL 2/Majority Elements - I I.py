n = int(input())
ar = list(map(int, input().split()))



def validCand(ar, n):
    v1 = ar[0]
    v2 = ar[0]
    c1 = 1
    c2 = 1
    for i in range(1, n):
        if (v1 == ar[i]):
            c1 += 1
        elif (v2 == ar[i]):
            c2 += 1
        else:
            if c1 == 0:
                v1 = ar[i]
                c1 = 1
            elif c2 == 0:
                v2 = ar[i]
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1

    return [v1, v2]

if n<3:
    print(list(set(ar)))
else:
    val = validCand(ar, n)
    c1 = 0
    c2 = 0
    for i in ar:
        if i == val[0]:
            c1 += 1
        elif i == val[1]:
            c2 += 1
    ans=[]
    if c1 > n//3:
        ans.append(val[0])
    if c2 > n//3:
        ans.append(val[1])
    print(ans)
