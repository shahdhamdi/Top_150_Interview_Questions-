class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert to lowercase
        s = s.lower()

        # Initialize two pointers
        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer to the next alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1
            # Move right pointer to the previous alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Check if characters at left and right pointers are equal
            if s[left] != s[right]:
                return False
            
            # Move pointers closer
            left += 1
            right -= 1

        return True
