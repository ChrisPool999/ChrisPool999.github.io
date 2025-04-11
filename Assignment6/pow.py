def pow(num: int, exp: int) -> float:
    # results in divide by zero error 
    if num == 0 and exp < 0:
        return None

    if exp == 0: 
        return 1

    sum = powHelp(num, abs(exp))
    if exp < 0: 
        return 1/sum 

    return sum   

def powHelp(num: int, exp: int) -> float:
    if exp == 1: 
        return num 

    half = powHelp(num, exp//2)
    sum = half * half

    if (exp % 2) != 0:
        sum *= num

    return sum


# test exponent 0
print(pow(-4, 0)) # expects: 1
print(pow(-47, 0)) # expects: 1
print(pow(4, 0)) # expects: 1
print(pow(47, 0)) # expects: 1

# test exponent 1
print(pow(0, 1)) # expects: 0
print(pow(4, 1)) # expects: 4
print(pow(-5, 1)) # expects: -5

# test basic exponent
print(pow(4, 2)) # expects: 16
print(pow(2, 5)) # expects: 32
print(pow(1, 9)) # expects: 1
print(pow(0, 3)) # expects: 0

# test negative exponent
print(pow(4, -2)) # expects: 1/16 or .0625
print(pow(2, -5)) # expects: 1/32 or .03125
print(pow(1, -9))# expects: 1