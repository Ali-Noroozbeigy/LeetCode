from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        sorted_prices = sorted(prices)
        sum = sorted_prices[0] + sorted_prices[1]
        if sum > money:
            return money
        return money - sum