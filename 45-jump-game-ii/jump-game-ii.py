class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        end = 0
        minJump = 0
        n = len(nums)
        
        # If only one element, no jump is needed
        if n == 1:
            return 0
        
        for i in range(n - 1):
            # Update the max reach from current index
            max = max(max, i + nums[i])
            
            # If we reach the end of the current jump range, make another jump
            if end == i:
                minJump += 1
                end = max
                
            # If the end point reaches or exceeds the last index, break
            if end >= n - 1:
                break
        
        return minJump