def is_closer(x: int, y: int, target: int) -> bool:
	return abs(x - target) < abs(y - target)

def find_closest(nums: list[int], target: int) -> int:
	left = 0
	while (left + 1 < len(nums) 
		and (nums[left] == nums[left + 1] or is_closer(nums[left + 1], nums[left], target))
	):
		left += 1

	return left

def k_closest(nums: list[int], k: int, x: int) -> list[int]:
	left = right = find_closest(nums, x)

	while (right - left) + 1 < k:
		if (left <= 0 
			or (right < len(nums) - 1 and is_closer(nums[right + 1], nums[left - 1], x))
		):
			right += 1
		else:
			left -= 1

	return nums[left: right + 1]

print(k_closest([1,2,3,4,5], 4, 3))
print(k_closest([1,2,3,4,5], 4, -1))
print(k_closest([1,2,3,4,4,4,4], 4, 4))
print(k_closest([1,1,1,1,2,3,4,4,4,4], 4, 1))
print(k_closest([1], 1, 1))