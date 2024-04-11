class Solution:
    def myAtoi(self, s: str) -> int:
        without_space = s.strip()

        result = []
        sign = 1

        sign_read = False

        for char in without_space:
            if char == "-" and not sign_read:
                sign = -1
                sign_read = True

            elif char == "+" and not sign_read:
                sign_read = True
                continue

            elif char.isnumeric():
                if not sign_read:
                    sign_read = True
                result.append(char)

            else:
                break

        try:
            digits = int("".join(result))

            if digits >= (2 ** 31):
                if sign == 1:
                    return (2 ** 31) - 1
                return -1 * (2 ** 31)
            return sign * digits
        except ValueError:
            return 0
