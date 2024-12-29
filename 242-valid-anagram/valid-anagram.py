class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSorted=sorted(s, reverse=True)
        tSorted=sorted(t, reverse=True)
        if(sSorted==tSorted):return True
        return False