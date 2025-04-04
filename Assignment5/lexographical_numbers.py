def lexographical_numbers(n: int) -> list[int]:
    lst = []
    for i in range(1, 10):
        lexographical_numbers_helper(n, lst, i)
    return lst

def lexographical_numbers_helper(end: int, result: list[int], curr: int, digit: int = 0) -> None:
    if curr > end: return 
    result.append(curr)

    for i in range(digit, 10):
        next = (curr * 10) + i        
        lexographical_numbers_helper(end, result, next, i)

print(lexographical_numbers(13))
print(lexographical_numbers(10))
print(lexographical_numbers(7))
print(lexographical_numbers(0))
print(lexographical_numbers(30))
print(lexographical_numbers(100))
