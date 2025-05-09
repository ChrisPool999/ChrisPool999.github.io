# 1. Course Schedule II

Time - O(N)    -->  Never does more than the amount of prerequesites 
Space - O(N)   -->  recursive stack space 

Approach:
- Exact same as course schedule 1, but build an array as we backtrack

- We use DSF, searching through course dependancies, until we hit a course with no dependancies or dependancies we've taken

- add them into the result array as we backtrack, the base case (class with no dependancies) will get added first
    - leading to classes only being added their dependancies are in the result array
- Mark all courses in that path as taken

- cycle detection: we simply record the depth as we recursively search for a class with satisfiable dependancies
    - if that depth goes over the amount of classes possible, we've already searched through all possible classes

# _______________________________________________________________________________________________________________________________________

# 2. Divide Two Integers

Time - O(log(y/x))   - We're multipying divisor by 2 multiple times, instead of just looping y - x and seeing how many times it takes
Space - O(1)

Approach:
- Idea: The brute force approach would just be doing a loop, and seeing how many times you can subtract x from y
- A way to make this faster, is to use bit manipulation to left shift divisor as many times as we can, unless it'd be bigger than divisor
        - left shifting ( << ) is equivilent to multiplying a number by 2
- so if the divisor can left shift 4 times, it means you can atleast fit it inside the dividend 16 times (1 >> 4) = 16
- set dividend as remainder, then reset the divisor back to original value
    
- example: divisor: 3, dividend: 60
    - 3 << 4 = 48
    - 1 << 4 = 16 (multiplier)
    - So 3 fits into 60 atleast 4 times
    - repeat with the remainer: 12
    - 3 << 3 = 12
    - 1 << 3 = 4 (multiplier) 

    quotient = 16 + 4 = 20

# _______________________________________________________________________________________________________________________________________

# 3. coin_change

TIme - O(N * amount)  --> for each amount possible, we'll at most try each coin on it
Space - O(amount)

Approach:
- We use backtracking to try every single combination of coins.
- we try every coin on each amount, saving the best into our cache

Code:
- to implement combinations, we use a for loop with a recursive approach
- we save the best from the for loop, adding it to our cache after
- we use an array where index = amount. Array is faster than a hashmap, but might use unneeded space