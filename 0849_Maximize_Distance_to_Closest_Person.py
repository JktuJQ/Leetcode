class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        previous = 0
        max_len = 0

        for i in range(len(seats)):
            if seats[i] == 1:
                if seats[previous] == 1:
                    max_len = max(max_len, (i - previous) // 2)
                else:
                    max_len = max(max_len, i - previous)
                previous = i
        if seats[previous] == 1:
            max_len = max(max_len, i - previous)
        return max_len
