def majority_element(arr: list[int]) -> int:
    major = None
    count = 0
    
    for n in arr:
        # if count == 0, we create a partition and solve the subproblem
        if count == 0:
            major = n
            count = 1
   
        elif n == major:
            count += 1
        else:
            count -= 1
    
    return major 

print(majority_element([8, 2, 8, 3, 8, 4, 8]))  # Majority: 8
print(majority_element([1, 2, 1, 3, 1, 4, 1, 5, 1]))  # Majority: 1 
print(majority_element([9, 1, 9, 2, 9, 3, 9, 4, 9, 5, 9]))  # Majority: 9 
print(majority_element([6, 2, 6, 3, 6, 4, 6, 6, 6, 6]))  # Majority: 6 
print(majority_element([4, 1, 4, 2, 4, 3, 4, 5, 4, 4, 4, 4]))  # Majority: 4 
print(majority_element([2, 3, 2, 4, 2, 5, 2, 6, 2, 7, 2, 2, 2]))  # Majority: 2 
print(majority_element([5, 1, 5, 2, 5, 3, 5, 4, 5, 6, 5, 7, 5, 8]))  # Majority: 5 

print(majority_element([5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 5]))  # Majority: 5 
print(majority_element([5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4]))  # Majority: 4
print(majority_element([3, 2, 3, 1, 3, 4, 3, 5, 3, 4, 3]))  # Majority: 3 
print(majority_element([3, 2, 2]))  # Majority: 2
print(majority_element([2, 3, 2]))  # Majority: 2
