class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        left=0
        right=rows*cols-1
        while(left<=right):
            mid=(left+right)//2
            mid_val=matrix[mid//cols][mid%cols]
            if(mid_val==target):
                return True
            if mid_val<target:
                left=mid+1
            elif mid_val>target:
                right=mid-1
        return False
