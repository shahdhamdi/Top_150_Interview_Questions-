## Problem Description

Given an integer array `nums`, we need to return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

### Constraints:
- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.


## Approach

To solve this problem without using division, we can break it into two passes: one for the prefix product and one for the suffix product. Here’s the detailed step-by-step approach:

### Steps:

1. **Initialize the result array:**
   - We create an array `ans` of the same length as `nums`, initialized with 1. This will store the final result, i.e., the product of all elements except the current one.

2. **First pass (Prefix Product):**
   - Traverse the array from left to right. 
   - For each index `i`, compute the product of all elements before it (the prefix product).
   - Store this running product in `ans[i]`.
   - For example, if the `nums` array is `[1, 2, 3, 4]`, after the first pass, `ans` will be `[1, 1, 2, 6]`, where each element stores the product of all elements to its left.

3. **Second pass (Suffix Product):**
   - Traverse the array from right to left.
   - For each index `i`, compute the product of all elements after it (the suffix product).
   - Multiply this suffix product with the value already stored in `ans[i]` from the first pass.
   - For example, after the second pass, the `ans` array will be updated with the final product values.

4. **Return the result:**
   - After both passes, the `ans` array will contain the product of all elements except the one at each index.


### Time Complexity:
- **O(n)**: We traverse the array twice, once for the prefix product and once for the suffix product.

### Space Complexity:
- **O(1)**: Since we are modifying the `ans` array in-place, the space complexity does not increase (excluding the output array).
