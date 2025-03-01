class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmapS={}
        hashmapT={}
        for letter in s:
            if letter not in hashmapS:
                hashmapS[letter]=1
            else:
                hashmapS[letter]+=1
        for letter in t:
            if letter not in hashmapT:
                hashmapT[letter]=1
            else:
                hashmapT[letter]+=1
        for letter in t:
            if letter not in s or hashmapS[letter]!=hashmapT[letter]:
                return letter