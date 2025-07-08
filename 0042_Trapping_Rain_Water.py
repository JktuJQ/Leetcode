class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0

        while left < right:
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])
            if max_left <= max_right:
                result += max_left - height[left]
                left += 1
            else:
                result += max_right - height[right]
                right -= 1
        return result
