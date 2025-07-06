class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = list()
        if len(nums) == 0:
            return ranges

        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                if start == nums[i - 1]:
                    ranges.append(f"{start}")
                else:
                    ranges.append(f"{start}->{nums[i - 1]}")
                start = nums[i]
        if start == nums[len(nums) - 1]:
            ranges.append(f"{start}")
        else:
            ranges.append(f"{start}->{nums[len(nums) - 1]}")
        
        return ranges
