class Solution:
    def trap(self, height: List[int]) -> int:
        trapped=0
        n=len(height)
        MaxRight=[0]*n
        MaxLeft=[0]*n
        MaxLeft[0]=height[0]
        MaxRight[n-1]=height[n-1]
        for i in range(1,n):
            MaxLeft[i]=max(height[i],MaxLeft[i-1])
        for i in range(n-2,-1,-1):
            MaxRight[i]=max(height[i],MaxRight[i+1])
        for i in range(n):
             minMax=min(MaxLeft[i],MaxRight[i])
             if (minMax-height[i]>0):
                trapped+=minMax-height[i]
            
        return trapped
