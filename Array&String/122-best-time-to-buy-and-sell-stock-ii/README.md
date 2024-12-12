# Best Time to Buy and Sell Stock II - README

## Problem Description

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i-th` day.

On each day, you may decide to buy and/or sell the stock. You can only hold **at most one** share of the stock at any time. However, you can buy it and immediately sell it on the **same day**.

Find and return the **maximum profit** you can achieve.

### Example 1:
```text
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: 
    Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5 - 1 = 4.
    Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6 - 3 = 3.
    Total profit is 4 + 3 = 7.

## Approach
- To solve this problem, we can iterate over the prices array and track when we can make a profit.

- If the price on day i is greater than the price on day i-1, then there is a profit to be made by buying on day i-1 and selling on day i.
- We accumulate the profit in a variable profit and return it at the end.

## Time and Space Complexity:
**Time Complexity**: O(n), where n is the number of days (length of the prices array). We iterate through the prices array once.
**Space Complexity**: O(1). We only use a few extra variables for tracking the profit, so the space complexity is constant.
