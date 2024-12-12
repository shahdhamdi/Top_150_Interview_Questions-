## Problem: Rotate Array

### Description:
Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

### Approach:
We can solve this problem using a **reverse** approach to perform the rotation in-place:
1. First, we reverse the entire array.
2. Then, we reverse the first `k` elements and the remaining elements from index `k` to the end of the array.
3. This effectively rotates the array to the right by `k` steps.

### Steps:
1. Reverse the entire array.
2. Reverse the first `k` elements (i.e., from index 0 to k-1).
3. Reverse the remaining elements (i.e., from index k to the end of the array).

This approach ensures that the rotation happens in-place with a time complexity of O(n) and space complexity of O(1).

### Time and Space Complexity:
- **Time Complexity**: O(n)
  - We perform three reverse operations, each taking O(n) time.
  
- **Space Complexity**: O(1)
  - The operation is done in-place, so no extra space is used other than a few pointers.

### Example:

#### Example 1:
**Input**: `nums = [1,2,3,4,5,6,7], k = 3`  
**Output**: `[5,6,7,1,2,3,4]`  
**Explanation**:  
- Rotate 1 step to the right: `[7,1,2,3,4,5,6]`
- Rotate 2 steps to the right: `[6,7,1,2,3,4,5]`
- Rotate 3 steps to the right: `[5,6,7,1,2,3,4]`

#### Example 2:
**Input**: `nums = [-1,-100,3,99], k = 2`  
**Output**: `[3,99,-1,-100]`  
**Explanation**:  
- Rotate 1 step to the right: `[99,-1,-100,3]`
- Rotate 2 steps to the right: `[3,99,-1,-100]`

### Constraints:
- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`


