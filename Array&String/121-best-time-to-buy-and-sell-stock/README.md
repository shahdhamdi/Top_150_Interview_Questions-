## Problem: Best Time to Buy and Sell Stock

### Description:
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i<sup>th</sup>` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return **the maximum profit** you can achieve from this transaction. If you cannot achieve any profit, return `0`.

### Example:

#### Example 1:
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


### Approach:
We can solve this problem using a **single pass** approach to find the maximum profit:

1. Initialize a variable `mn` to a very large value (100000), which will track the minimum price encountered so far.
2. Initialize `ans` to 0, which will hold the maximum profit.
3. Loop through the array `prices`:
   - If the current price is less than `mn`, update `mn` to the current price.
   - If the current price is greater than `mn`, calculate the potential profit (`current price - mn`) and update `ans` if this profit is greater than the current `ans`.
4. Return `ans` as the result.

### Time and Space Complexity:
- **Time Complexity**: O(n)
  - We iterate through the array only once.
- **Space Complexity**: O(1)
  - We only use a constant amount of space to store variables.
