def longestCommonPrefix(strs: list[str]) -> str:
    i = 0
    while True:
        if i >= len(strs[0]):
            return strs[0][:i]
        
        current = strs[0][i]

        for s in strs:
            if i >= len(s) or s[i] != current:
                return strs[0][:i]

        i += 1

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
print(longestCommonPrefix(["","flo","flower"]))
print(longestCommonPrefix(["ff","fffff","fffff"]))


"""
Time - O(N * M) where M = avg word size, N = number of strings
Space - O(1) - No space used

Approach:
- We first make sure all strings' first index is matching, then second index, until
        we reach a mismatch, or we reach a string that has ended
- the way the loop goes, it goes through every string for index 0, 
        then every string for index 1... and so on

"""