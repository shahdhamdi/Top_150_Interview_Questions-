class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n= len(numbers)
        s=0
        e=n-1
        while s < e:
            sum=numbers[s]+numbers[e]
            if sum==target:
                #Return 1-based indecies
                return [s+1,e+1]
            elif sum<target:
                s+=1
            else:
                e-=1
