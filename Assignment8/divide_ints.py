def divide(dividend: int, divisor: int) -> int:
    sign = 1 if (dividend > 0) == (divisor > 0) else -1
    dividend, divisor = abs(dividend), abs(divisor)

    result = 0
    while dividend >= divisor:
        temp = divisor
        multiplier = 1

        # left shift = divisor can fit into dividend (1 << multiplier) times 
        while (temp << 1) <= dividend:
            temp <<= 1
            multiplier <<= 1

        # turn dividend into remainder and keep going
        dividend -= temp
        result += multiplier

    return sign * result

# BASIC
print(divide(7, 3)) # expects: 2
print(divide(10, 2)) # expects: 5

# CHECK NEGATIVES
print(divide(-10, 2)) # expects: -5
print(divide(10, -2)) # expects: -5
print(divide(-10, -1)) # expects: 10

# DIVISOR > DIVIDEND
print(divide(10, 12)) # expects: 0

# DIVIDE BY ONE
print(divide(10, 1)) # expects: 10
