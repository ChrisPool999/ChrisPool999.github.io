def find_position(nums: list[int], target: int, find_start: bool = True) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            if find_start:
                if mid == 0 or nums[mid - 1] != target:
                    return mid
                right = mid - 1
            else:
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    return mid
                left = mid + 1

    return -1


def first_and_last(nums: list[int], target: int) -> tuple[int, int]:
    start = find_position(nums, target)
    end = find_position(nums, target, find_start=False)
    return (start, end)

def main():
    print(first_and_last([1, 2, 2, 2, 3], 2))       # Expected: 1, 4
    print(first_and_last([5, 7, 7, 8, 8, 10], 8))   # Expected: 3, 4
    print(first_and_last([1, 1, 1, 1, 1], 1))       # Expected: 0, 4

    print(first_and_last([1, 2, 3, 4, 5], 1))       # Expected: 0, 0
    print(first_and_last([1, 2, 3, 4, 5], 5))       # Expected: 4, 4
    print(first_and_last([2, 2, 2, 2, 2], 2))       # Expected: 0, 4

    print(first_and_last([1, 3, 5, 7], 2))          # Expected: -1, -1
    print(first_and_last([], 3))                    # Expected: -1, -1

    nums = [1] * 1000000 + [2] * 1000000
    print(first_and_last(nums, 2))                  # Expected: 1000000, 1999999

    print(first_and_last([3], 3))                   # Expected: 0, 0
    print(first_and_last([4], 3))                   # Expected: -1, -1

if __name__ == "__main__":
    main()