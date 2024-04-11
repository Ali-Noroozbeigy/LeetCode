class Solution:
    def isValid(self, s: str) -> bool:

        openings = ["(", "{", "["]
        closing = {")": "(", "}": "{", "]": "["}

        stack = []

        for char in s:
            if char in openings:
                stack.append(char)

            # stack is empty
            elif len(stack) == 0:
                return False

            else:
                last_char = stack.pop()
                if last_char != closing[char]:
                    return False

        if len(stack) == 0:
            return True

        return False