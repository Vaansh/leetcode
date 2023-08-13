class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = "".join(c.lower() for c in s if c.isalnum())
        return tmp == tmp[::-1]
