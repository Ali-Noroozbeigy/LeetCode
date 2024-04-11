class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = -1
        
        for customer in accounts:
            s = sum(customer)
            if s > max_wealth:
                max_wealth = s

        return max_wealth