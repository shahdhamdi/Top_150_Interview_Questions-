class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst=[]
        hashmap={}
        for num in nums2:
            if num not in hashmap:
                hashmap[num]=1
            else:
                hashmap[num]+=1
        for num in nums1:
            if num in hashmap and hashmap[num]>0:
                lst.append(num)
                hashmap[num]-=1
        return lst