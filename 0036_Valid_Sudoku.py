class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for r in range(9)]
        cols = [set() for c in range(9)]
        boxes = [set() for box in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                elem = board[r][c]
                box = 3 * (r // 3) + (c // 3)

                if elem in rows[r] or elem in cols[c] or elem in boxes[box]:
                    return False
                rows[r].add(elem)
                cols[c].add(elem)
                boxes[box].add(elem)
        return True
