## Problem: Remove Duplicates from Sorted Array

### Description:
Given a sorted array `nums`, remove the duplicates in-place so that each unique element appears only once. Return the number of unique elements.

### Approach:
1. **Two-Pointer Technique**: Use a pointer `k` to track the position of unique elements.
2. **Iterate Through the Array**: For each element, if it's different from the previous one, place it at index `k` and increment `k`.
3. **Return `k`**: The first `k` elements will be the unique elements.

### Time and Space Complexity:
**Time Complexity**: O(n)
**Space Complexity**: O(1)

