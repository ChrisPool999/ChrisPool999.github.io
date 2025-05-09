def coin_change_helper(coins: list[int], amount: int, cache: list[int]) -> int:
    if not amount:
        return 0
    
    if amount < 0:
        return -1
    
    if cache[amount]:
        return cache[amount]
    
    best = -1
    for coin in coins:
        result = coin_change_helper(coins, amount - coin, cache)

        if result != -1:
            best = result + 1 if best == -1 else min(best, result + 1)

    cache[amount] = best
    return best

def coinChange(coins: list[int], amount: int) -> int:
    cache = [0] * (amount + 1)
    return coin_change_helper(coins, amount, cache)

# BASIC
print(coinChange([1,2,5], 11)) # expects: 3

# CAN'T REACH 0
print(coinChange([2], 3)) # expects: -1
print(coinChange([2], 1)) # expects: -1

# AMOUNT = 0
print(coinChange([1], 0)) # expects: 0

# VERIFY RETURNS BEST 
print(coinChange([1, 2, 3, 4, 5], 5)) # expects: 1
print(coinChange([1, 2, 3, 4, 5], 7)) # expects: 2