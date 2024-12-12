## Problem: H-Index

### Description:
Given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their `i-th` paper, return the researcher's **h-index**.

The **h-index** is defined as the maximum value of `h` such that the given researcher has published at least `h` papers that have each been cited at least `h` times.

### Approach:
To calculate the **h-index**:
1. Sort the `citations` array in descending order.
2. Iterate over the sorted array and check if the number of papers with citations greater than or equal to the current index is at least the value of the index. The point where this condition fails gives the h-index.

### Steps:
1. Sort the `citations` array in decreasing order.
2. Iterate through the array:
   - For each paper, check if the number of papers greater than or equal to the current index is less than or equal to the index.
3. If the condition is met, return the index as the h-index.
4. If no such index is found, the h-index is the length of the array.

### Time and Space Complexity:
- **Time Complexity**: O(n log n)  
  - Sorting the array takes O(n log n) time.
  
- **Space Complexity**: O(1)  
  - The operation is done in-place, so no extra space is used.

### Example:

#### Example 1:
**Input**: `citations = [3, 0, 6, 1, 5]`  
**Output**: `3`  
**Explanation**:  
- The researcher has 5 papers, and the citation counts are [3, 0, 6, 1, 5].
- The h-index is 3 because there are 3 papers with at least 3 citations.

#### Example 2:
**Input**: `citations = [1, 3, 1]`  
**Output**: `1`  
**Explanation**:  
- The researcher has 3 papers, and the citation counts are [1, 3, 1].
- The h-index is 1 because there is 1 paper with at least 1 citation.

### Constraints:
- `n == citations.length`
- `1 <= n <= 5000`
- `0 <= citations[i] <= 1000`

