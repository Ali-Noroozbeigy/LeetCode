class Solution:
    def isPalindrome(self, x: int) -> bool:
        as_str = str(x)
        return as_str == as_str[::-1]