class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        it=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[it]=nums[i]
                it+=1
               
        return it

