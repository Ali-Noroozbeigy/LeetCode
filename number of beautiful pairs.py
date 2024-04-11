import math

def num(nums):
    total = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if math.gcd(int(str(nums[i])[0]), int(str(nums[j])[-1])) == 1:
                total += 1
    return total