class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash1={}
        hash2={}
        n=len(s)
        for i in range(n):
            ch1,ch2=s[i],t[i]
            if ch1 in hash1 and hash1[ch1]!=ch2 or ch2 in hash2 and hash2[ch2] !=ch1:
                return False
            else:
                hash1[ch1]=ch2
                hash2[ch2]=ch1
        return True