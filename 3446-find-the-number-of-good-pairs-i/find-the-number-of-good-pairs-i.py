class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans=0
        for num in nums1:
            for num2 in nums2:
                if num%(num2*k)==0:
                    ans+=1
        return ans
