class Solution:
    def shuffle(self, nums, n):
        result = []
        for i in range(n):
            result.append(nums[i])    # Append x[i]
            result.append(nums[i + n])  # Append y[i]
        return result
