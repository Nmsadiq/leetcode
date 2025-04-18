class Solution:
    def countKDifference(self, nums, k):
        freq = {}
        count = 0

        for num in nums:
            # Check if (num - k) or (num + k) has been seen before
            count += freq.get(num - k, 0)
            count += freq.get(num + k, 0)

            # Store the current number in frequency map
            freq[num] = freq.get(num, 0) + 1

        return count
