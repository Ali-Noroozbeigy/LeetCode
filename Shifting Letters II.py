from collections import defaultdict
from typing import List
import string


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s_as_list = list(s)
        self.alphabets = list(string.ascii_lowercase)  # ['a', 'b', ..., 'z']
        self.len_alpha = len(self.alphabets)

        difference_array = [0] * (len(s) + 1)

        for start, end, direction in shifts:
            value = 1 if direction == 1 else -1
            difference_array[start] += value
            difference_array[end+1] -= value

        for i in range(1, len(difference_array)):
            difference_array[i] += difference_array[i-1]

        for i in range(len(s)):
            s_as_list[i] = self.shift(s_as_list[i], difference_array[i])

        return "".join(s_as_list)

    def shift(self, char, num_shift):
        return self.alphabets[(ord(char) - 97 + num_shift) % self.len_alpha]


s = Solution()
print(s.shiftingLetters("dztz", [[0,0,0],[1,1,1]]))
