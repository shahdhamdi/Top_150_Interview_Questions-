class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int: 
        hashset=set(allowed)
        ans=0
        for word in words:
            flag=True
            for letter in word:
                if letter not in hashset:
                    flag=False
                    break
            if flag:
                ans+=1
        return ans
        
        
        