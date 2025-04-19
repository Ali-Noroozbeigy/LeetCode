class Solution:
    def compressedString(self, word: str) -> str:
        comb = []

        seq_count = 1
        current_char = word[0]
        for i in range(1, len(word)):
            if word[i] == current_char:
                seq_count += 1
                if seq_count == 10:
                    comb.append(str(seq_count-1))
                    comb.append(current_char)
                    seq_count = 1

            else:
                comb.append(str(seq_count))
                comb.append(current_char)
                seq_count = 1
                current_char = word[i]
        comb.append(str(seq_count))
        comb.append(current_char)
        return "".join(comb)

s = Solution()
print(s.compressedString("abcde"))
