## Problem: Majority Element

### Description:
Given an array `nums` of size `n`, return **the majority element**.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

### Approach:
We can solve this problem using a **hash map** to count the frequency of each element:
1. Iterate through the array `nums` and count the frequency of each element using an unordered map.
2. Once we have the frequency of each element, we check which element appears more than `n/2` times. This is the majority element.
3. Return the majority element.

### Time and Space Complexity:
- **Time Complexity**: O(n)
  - We traverse the array `nums` twice, once for counting the frequency and once for checking the frequency.
  
- **Space Complexity**: O(n)
  - We use a hash map to store the frequency of each element, which could require space proportional to the size of the input array.

### Example:

#### Example 1:
**Input**: `nums = [3,2,3]`  
**Output**: `3`  
**Explanation**: The element `3` appears 2 times which is more than `⌊3 / 2⌋ = 1` time.

#### Example 2:
**Input**: `nums = [2,2,1,1,1,2,2]`  
**Output**: `2`  
**Explanation**: The element `2` appears 4 times which is more than `⌊7 / 2⌋ = 3` times.

### Constraints:
- `n == nums.length`
- `1 <= n <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`

