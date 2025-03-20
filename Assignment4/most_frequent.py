def most_frequent(nums: list[int], k: int) -> list[int]:
	map = {}
	for n in nums:
		if n in map:
			map[n] += 1
		else:
			map[n] = 1

	bucket = [[] for _ in range(len(nums))]
	for value, count in map.items():
		if bucket[count-1]:
			bucket[count-1].append(value)
		else:
			bucket[count-1] = [value]

	result = []
	for i in range (len(bucket)):
		for n in bucket[len(bucket) - i - 1]:
			result.append(n)
			if len(result) == k:
				return result
		
print(most_frequent([1], 1))
print(most_frequent([1, 2], 1))
print(most_frequent([1, 2, 2, 1], 2))

print(most_frequent([1], 1))
print(most_frequent([1, 2], 1))
print(most_frequent([1, 2, 2, 1], 2))

print(most_frequent([1, 1, 1], 1))
print(most_frequent([1, 2], 2))
print(most_frequent([1, 2, 2, 1], 1))
