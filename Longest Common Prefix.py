class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        first_str = strs[0]
        longest_prefix = ""

        for i in range(1, len(first_str) + 1):
            if self.is_in_others(first_str[0:i], strs):
                longest_prefix = first_str[0:i]
            else:
                break

        return longest_prefix

    def is_in_others(self, selected_str: str, strs: List[str]) -> bool:
        for i in range(1, len(strs)):
            if not strs[i].startswith(selected_str):
                return False
        return True
