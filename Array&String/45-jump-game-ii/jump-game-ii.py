class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max=0
        end=0
        minJump=0
        n=len(nums)
        if(n==1):
            return 0
        for i in range(n-1):
            if max<i+nums[i]:
                max=i+nums[i]
            if end==i:
                minJump+=1
                end=max
            if end>=n-1:
                break
        return minJump
            
        