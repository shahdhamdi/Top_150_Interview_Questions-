class Solution:
    def romanToInt(self, s: str) -> int:
        roman_nums={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        n=len(s)-1
        ans=0
        ans+=roman_nums[s[n]]
        for i in range(n):
            if roman_nums[s[i]]<roman_nums[s[i+1]]:
                ans-=roman_nums[s[i]]
            else:
                ans += roman_nums[s[i]]
        return ans
