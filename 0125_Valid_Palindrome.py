class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while not s[left].lower().isalnum():
                left += 1
                if left > right:
                    return True
            while not s[right].lower().isalnum():
                right -= 1
                if right < left:
                    return True
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
