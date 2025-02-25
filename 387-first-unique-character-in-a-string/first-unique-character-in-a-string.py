class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap={}
        for i,letter in enumerate(s):
            if letter not in hashmap:
                hashmap[letter]=1
            else:
                hashmap[letter]+=1
        for i,letter in enumerate(s):
            if hashmap[letter] == 1:
                return i
        return -1