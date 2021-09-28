class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l=len(s)
        d={}
        for i in range(l):
            d[s[i]]=i
        ans=[]
        i=0
        pre=-1
        m=0
        while i< l:
            if i>m :
                ans.append(m-pre)
                pre= m
                m=d[s[i]]
            if m< d[s[i]]:
                m=d[s[i]]
        
            
            i+=1
        ans.append(m-pre)
        return ans
                
            
