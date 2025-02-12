import collections


class Solution:
    def minimizeStringValue(self, s: str) -> str:
        count_of_words = collections.Counter(s)
        alphabets = [chr(i) for i in range(97, 123)]  # Lowercase a-z
        candidates = []

        for i, c in enumerate(s):
            if c == '?':
                min_char, min_repeat = "", float('inf')
                # finding the least repeated char
                for a in alphabets:
                    if count_of_words[a] < min_repeat:
                        min_char, min_repeat = a, count_of_words[a]
                count_of_words[min_char] += 1
                candidates.append(min_char)

        candidates = sorted(candidates)
        j = 0
        s_arr = list(s)
        for i, c in enumerate(s_arr):
            if c == "?":
                s_arr[i] = candidates[j]
                j += 1
        return "".join(s_arr)


s = Solution()
print(s.minimizeStringValue("abcdefghijklmnopqrstuvwxy??"))
