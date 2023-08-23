class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = "".join(c.lower() for c in s if c.isalnum())
        return res == res[::-1]
