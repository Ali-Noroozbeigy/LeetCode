def longest_substring(s: str):
    i = 0
    longest = 0
    current_sub = []
    while i < len(s):
        j = i
        while j < len(s):
            if s[j] not in current_sub:
                current_sub.append(s[j])
                j += 1
            else:
                if len(current_sub) > longest:
                    longest = len(current_sub)
                current_sub = []
                i += 1
                break
    return longest

