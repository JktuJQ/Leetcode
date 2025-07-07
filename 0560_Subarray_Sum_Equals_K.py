from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        
        prefixes = defaultdict(int)
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum == k:
                count += 1
            if current_sum - k in prefixes:
                count += prefixes[current_sum - k]
            prefixes[current_sum] += 1
        return count
