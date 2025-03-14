class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq={}
        ans=[]
        for num in nums:
            if num in freq:
                ans.append(num)
            else:
                freq[num]=1
        return ans