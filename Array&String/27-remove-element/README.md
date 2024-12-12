## Problem: Remove Element

### Description:
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` **in-place**. The order of the elements may be changed. Then return the number of elements in `nums` that are not equal to `val`.

### Approach:
1. **Two Pointer Technique**: used a pointer `it` to track the position where the next element (that is not equal to `val`) should be placed.
2. **Iterate Through the Array**: Traverse through the array, and each time an element is not equal to `val`, place it at index `it` and increment `it`.
3. **Return the Count**: The pointer `it` will indicate how many elements are not equal to `val`.

### Time and Space Complexity:
**Time Complexity**: O(n)
**Space Complexity**: O(1)
