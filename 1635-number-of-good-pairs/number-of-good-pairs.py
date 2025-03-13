class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums_indexes={}
        ans=0
        for i,num in enumerate(nums):
            if num in nums_indexes:
                ans+=nums_indexes[num]
                nums_indexes[num]+=1
            else:
                nums_indexes[num]=1
        return ans
