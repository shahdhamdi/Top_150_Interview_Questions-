## Problem Description

Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise.

A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.

### Example 1:

**Input**: `s = "abc", t = "ahbgdc"`  
**Output**: `true`  
Explanation: "abc" is a subsequence of "ahbgdc".

### Example 2:

**Input**: `s = "axc", t = "ahbgdc"`  
**Output**: `false`  
Explanation: "axc" is not a subsequence of "ahbgdc".

---

## Approach

To check if `s` is a subsequence of `t`, we can use a two-pointer technique:

1. **Initialize two pointers**:
   - `i` for string `s` (subsequence string).
   - `j` for string `t` (the main string).
   
2. **Traverse through `t`**:
   - If the characters `s[i]` and `t[j]` match, move to the next character in `s` by incrementing `i`.
   - Always increment `j` to move through the string `t`.
   
3. **Check if all characters of `s` are matched**:
   - If at any point `i` reaches the length of `s`, that means all characters of `s` have been found in `t` in order, and `s` is a subsequence of `t`.
   
4. **Return the result**:
   - If `i` reaches the end of `s`, return `true`.
   - Otherwise, return `false`.

