class Solution:
    def numIdenticalPairs(self, nums):
        freq = {}
        count = 0

        for num in nums:
            count += freq.get(num, 0)
            freq[num] = freq.get(num, 0) + 1

        return count
