## Problem: Merge Sorted Array

### Description:
You are given two integer arrays `nums1` and `nums2`, both sorted in **non-decreasing order**, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

You need to **merge** `nums1` and `nums2` into a single array sorted in **non-decreasing order**. The merged array should be stored in `nums1`. The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`.

To accommodate the merging, `nums1` has a length of `m + n`, where the first `m` elements represent the values that need to be merged, and the last `n` elements are set to 0 and should be ignored. `nums2` has a length of `n`.

### Approach:
We can solve this problem using a **two-pointer technique**:
1. We will use a pointer (`idx`) to iterate from the end of the array `nums1` (since the last `n` elements are zeros).
2. We compare elements from the end of both arrays (`nums1` and `nums2`), and place the larger element at the `idx` position in `nums1`.
3. We then move the corresponding pointer (`m` for `nums1` or `n` for `nums2`) backward and continue until we have merged all elements.
4. If there are any remaining elements in `nums2`, they will be placed into `nums1`.

### Time and Space Complexity:

- **Time Complexity**: O(m + n)
  - We iterate through both arrays (`nums1` and `nums2`) only once.
  
- **Space Complexity**: O(1)
  - Since the modification is done directly on the `nums1` array without needing extra space for another array.

