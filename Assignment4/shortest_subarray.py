from collections import deque

def shortest_subarray(nums: list[int], k: int) -> list[int]:	
	result = float("inf")
	dq = deque()
	sum = 0

	for i in range(len(nums)):
		sum += nums[i]
		if sum >= k:
			result = min(result, i + 1)

		# delete smallest prefix-sum, wont be needed again, for future uses, would only result in larger subarrays
		while dq and (sum - dq[0][0]) >= k:
			start = dq.popleft()[1]
			result = min(result, i - start)

		# maintain monotonic increasing
		# prefix sums that are smaller are more optimal, because subtracking the prefix-sum (partition it) results in higher subarray sum, with lower range
		while dq and dq[-1][0] >= sum:
			dq.pop()
		
		dq.append((sum, i))

	if result == float("inf"):
		return -1
	return result

print(shortest_subarray([3, 2, -4], 5))
print(shortest_subarray([3, 2, -4], 3))
print(shortest_subarray([1], 3))
print(shortest_subarray([3], 3))
print(shortest_subarray([84,-37,32,40,95], 167))
print(shortest_subarray([4,-14,7,-14,4], 7))