class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = list()

        intervals.sort(key=lambda interval: interval[0])
        result.append(intervals[0])
        for interval in intervals[1:]:
            if interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        return result
