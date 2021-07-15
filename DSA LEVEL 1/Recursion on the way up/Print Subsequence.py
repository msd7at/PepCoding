def prn(i,n,s):
    if len(n)==i:
        print(s)
        return
        # return a
    prn(i+1,n,s+n[i])
    prn(i+1,n,s)
    
    
    
    # return a



if __name__ == "__main__":
   n=input()
   prn(0,n,"")
#    print(s)

