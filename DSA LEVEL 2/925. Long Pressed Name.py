class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i=0
        j=0
        if len(name) > len(typed):
            return False
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i+=1
                j+=1
            elif j>0 and name[i-1] == typed[j]:
                j+=1
            else:
                return False
        if i<len(name):
            return False
        while j<len(typed):
            if name[-1] == typed[j]:
                j+=1
            else:
                return False
        return True
