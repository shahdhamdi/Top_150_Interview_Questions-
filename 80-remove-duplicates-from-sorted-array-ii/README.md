## Problem: Remove Duplicates from Sorted Array II

### Description:
Given an integer array `nums` sorted in **non-decreasing order**, remove some duplicates **in-place** such that each unique element appears **at most twice**. The **relative order** of the elements should be kept the **same**.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the **first part** of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` after placing the final result in the first `k` slots of `nums`.

### Approach:
We can use a two-pointer technique to solve this problem:
1. **Pointer `count`** will keep track of the number of elements that should remain in the array (i.e., non-duplicate elements).
2. As we iterate through the array, we check if the current element can be added to the result by ensuring it does not appear more than twice.


### Time and Space Complexity:
**Time Complexity**: O(n)
**Space Complexity**: O(1)
