#not my cleanest code but I learned about how to use global variables in Ptyhon correctly for leetcode/maybe other coding challenges in the future
class Solution:
    def __init__(self):
        self.dictionary = {}
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount in self.dictionary.keys():
            return self.dictionary[amount]
        
        least = -1
        for i in coins:
            if i <= amount:
                val = self.coinChange(coins, amount - i)
                if val == -1 : continue
                val += 1
                least = val if least == -1 else min(least, val)     
        self.dictionary[amount] = least
        print (str(amount) + ',' + str(least))
        return least