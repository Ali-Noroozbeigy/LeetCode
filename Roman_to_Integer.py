class Solution:
    def romanToInt(self, s: str) -> int:
        length = len(s)
        i = 0
        sum = 0

        while i < length:
            if self.is_exception(s, i):
                sum += symbol_value[s[i+1]] - symbol_value[s[i]]
                i += 2
            else:
                sum += symbol_value[s[i]]
                i += 1
        return sum

    def is_exception(self, s: str, i: int) -> bool:
        if i < len(s) - 1:
            return  (s[i] == "I" and s[i+1] == "V") or \
                    (s[i] == "X" and s[i + 1] == "L") or \
                    (s[i] == "I" and s[i+1] == "X") or\
                    (s[i] == "X" and s[i+1] == "C") or \
                    (s[i] == "C" and s[i+1] == "D") or\
                    (s[i] == "C" and s[i+1] == "M")
        else:
            return False


symbol_value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
