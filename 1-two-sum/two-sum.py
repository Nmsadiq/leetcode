class Solution:
    def twoSum(self, nums, target):
        seen = {}  # Dictionary to store number and its index
        for index, value in enumerate(nums):
            difference = target - value
            if difference in seen:
                return [seen[difference], index]
            seen[value] = index
