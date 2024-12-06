# Valid Palindrome 
## Problem Description

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a **palindrome**, or `false` otherwise.

### Example 1:
```text
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

## Approach

The approach to solving this problem involves the following steps:

1. **Normalize the string:** 
   - Convert all characters to lowercase.
   - Remove all non-alphanumeric characters. 
   - This is achieved using a list comprehension to filter out non-alphanumeric characters and convert the rest to lowercase.

2. **Check if the string is a palindrome:** 
   - After the string has been normalized, compare it with its reverse. 
   - If both the normalized string and its reverse are the same, it is a palindrome.
