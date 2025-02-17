class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        hashmap={}
        for i,num in enumerate(nums):
            if target-num in hashmap and hashmap[target-num]!=i :
                return [i,hashmap[target-num]]
            else:
                hashmap[num]=i