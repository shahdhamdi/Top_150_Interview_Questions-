class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return strs
        key={}
        for word in strs:
            sorted_word=tuple(sorted(word))
            if sorted_word not in key:
                key[sorted_word]=[]
            key[sorted_word].append(word)
        return list(key.values())        