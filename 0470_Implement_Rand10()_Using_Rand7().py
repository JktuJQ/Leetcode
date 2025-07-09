class Solution:
    def rand10(self) -> int:
        while True:
            r1 = rand7() - 1
            r2 = (rand7() - 1) * 7
            result = r1 + r2
            if result < 40:
                return (result % 10) + 1
