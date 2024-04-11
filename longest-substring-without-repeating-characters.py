class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        chars = set()

        longest = 0

        left_pointer = 0

        for right_pointer in range(len(s)):
            while s[right_pointer] in chars:
                chars.remove(s[left_pointer])
                left_pointer += 1
            chars.add(s[right_pointer])
            longest = max(longest, right_pointer - longest + 1)
        return longest
