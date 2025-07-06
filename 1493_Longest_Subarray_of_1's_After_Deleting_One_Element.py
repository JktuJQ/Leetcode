class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0
        start_index = 0
        last_zero = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                start_index = last_zero + 1
                last_zero = i
            longest = max(longest, i - start_index)
        return longest
