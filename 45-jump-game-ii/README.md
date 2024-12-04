## Problem: Jump Game II

### Description:
You are given a **0-indexed** array of integers `nums` of length `n`. You are initially positioned at `nums[0]`.

Each element `nums[i]` represents the maximum length of a forward jump from index `i`. In other words, if you are at `nums[i]`, you can jump to any `nums[i + j]` where:
- `0 <= j <= nums[i]` 
- `i + j < n`

Return the **minimum number of jumps** to reach `nums[n - 1]`. It is guaranteed that you can reach `nums[n - 1]`.

### Approach:
We can solve this problem using a greedy approach:
1. **Tracking the Maximum Reach**: At each step, track the farthest index you can reach from the current position.
2. **Updating the End Point**: Whenever you reach the end of the current jump, increment the jump count and set the new end to the farthest index you can reach.
3. **Terminate Early**: If the end point reaches or exceeds the last index, stop and return the jump count.

### Time and Space Complexity:
**Time Complexity**: O(n)
**Space Complexity**: O(1)