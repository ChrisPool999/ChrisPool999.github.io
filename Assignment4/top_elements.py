import heapq
import queue

def add_child(heap: list[int], map: dict, value: int, index: int) -> None:
	heapq.heappush(heap, -value)
	
	if value not in map:
		map[value] = queue.Queue()
		map[value].put(index)
	else:
		map[value].put(index)

def top_elements(nums: list[int], k: int) -> list[int]:
	if k < 0 or k > len(nums):
		raise ValueError("k must between 1 and length of list")

	result = []

	# mark negative to get max_heap (heapq only supports min heap)
	max_heap = [-nums[0]]

	# queue for duplicates
	value_to_index = {nums[0] : queue.Queue()}
	value_to_index[nums[0]].put(0)

	while len(result) != k:
		root = -(heapq.heappop(max_heap))
		result.append(root)
		root_index = value_to_index[root].get()

		left = (root_index * 2) + 1
		right = (root_index * 2) + 2

		if left < len(nums):
			add_child(max_heap, value_to_index, nums[left], left)
		if right < len(nums):
			add_child(max_heap, value_to_index, nums[right], right)

	return result

print(top_elements([15, 13, 12, 10, 8, 9], 5))
print(top_elements([10, 7, 9, 3, 6, 8, 5], 5))
print(top_elements([20, 18, 15, 10, 12, 14, 13, 5, 8, 9, 11], 8))
print(top_elements([10], 1))
print(top_elements([3, 2, 3, 2, 2, 2, 2], 4))
print(top_elements([10, 8, 8], 3))
