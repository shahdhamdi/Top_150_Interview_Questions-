class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=str(x)
        reversd_num=num[::-1]
        if reversd_num==num:
            return True
        else:
            return False