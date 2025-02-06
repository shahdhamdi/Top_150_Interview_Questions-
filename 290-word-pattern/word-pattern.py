class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        hash1={}
        hash2={}
        n=len(pattern)
        if n != len(words):
            return False
        for i in range(n):
            if pattern[i] in hash1 and hash1[pattern[i]]!=words[i] or words[i] in hash2 and hash2[words[i]]!= pattern[i]:
                return False
            else:
                hash1[pattern[i]]=words[i]
                hash2[words[i]]=pattern[i]
        return True