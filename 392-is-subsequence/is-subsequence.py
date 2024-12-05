class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        n=len(s)-1
        if s=="":
            return True
        for i in range(len(t)):
            if t[i]==s[j]:
                j+=1
            if j>n:return True
        return False
