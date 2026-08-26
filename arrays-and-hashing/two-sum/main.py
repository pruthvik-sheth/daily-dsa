


def two_sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        diff = target - nums[i]

        if diff in seen:
            return [seen[diff], i]

        seen[nums[i]] = i

# Time Complexity: O(n)
# Space Complexity: O(n)