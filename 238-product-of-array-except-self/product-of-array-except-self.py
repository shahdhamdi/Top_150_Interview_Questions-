class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product=[]
        suffix_product=[]
        n=len(nums)
        i=0
        for i in range(n):
            if i==0:
                prefix_product.append(1)
            else:
                prefix_product.append(nums[i-1]*prefix_product[i-1])
        j=n
        for j in range(-1,-n-1,-1):
            if(j==-1):
                suffix_product.append(1)
            else:
                suffix_product.append(nums[j+1]*suffix_product[-1])
            print(suffix_product[-1])

        suffix_product.reverse()
        i=0
        ans=[] 
        for num in suffix_product:
            ans.append(num*prefix_product[i])
            i=i+1
            
    
        return ans
