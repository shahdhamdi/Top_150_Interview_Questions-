class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        new_s=''
        for letter in s:
            if letter in 'abcdefghijklmnopqrstuvwxyz0123456789':
                new_s+=letter
        n=len(new_s)-1
        print(new_s)
        for i in range(len(new_s)):
            if new_s[i]!=new_s[n] and i<=n:
                #print(new_s[i],new_s[n])
                return False
            else:
                n=n-1
        return True
            
