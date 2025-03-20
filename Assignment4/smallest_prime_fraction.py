def smallest_prime_fraction(nums: list[int], k: int) -> list[int]:
	fractions = []
	for i in range(len(nums)):
		for j in range(i + 1, len(nums)):
			fractions.append((nums[i] / nums[j], [nums[i], nums[j]]))

	fractions = sorted(fractions, key=lambda x: x[0])

	if k >= len(fractions):
		return None

	return fractions[k-1][1]


print(smallest_prime_fraction([1,2,3,5], 3))
print(smallest_prime_fraction([1,7], 1))
print(smallest_prime_fraction([], 1))