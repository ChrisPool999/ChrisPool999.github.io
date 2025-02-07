
def two_sum(nums: list[int], target: int) -> tuple[int, int] :

    # seen maps the value to the index it occured
    seen = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in seen:
            return (seen[complement], i)

        seen[nums[i]] = i

def main():
    nums = [2,7,11,15]

    print(two_sum(nums, 9))  # expects (0, 1)
    print(two_sum(nums, 13)) # expects (0, 2)
    print(two_sum(nums, 17)) # expects (0, 3)
    print(two_sum(nums, 18)) # expects (1, 2)
    print(two_sum(nums, 22)) # expects (1, 3)
    print(two_sum(nums, 26)) # expects (2, 3)
    print("\n")

    # test negative numbers
    nums = [-2,7,-11,15]
    print(two_sum(nums, -13)) # expects (0, 2)
    print(two_sum(nums, 13))  # expects (0, 3)
    print(two_sum(nums, -4))  # expects (1, 2)
    print(two_sum(nums, 4))   # expects (2, 3)


if __name__ == "__main__":
  main()