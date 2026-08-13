class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check row condition
        for row in board:
            # Numbers already seen
            visited = set()
            for num in row:
                if num != '.' and num in visited:
                    return False
                
                visited.add(num)

        # Check column condition
        for col_idx in range(9):
            visited = set()
            for row in board:
                if row[col_idx] != '.' and row[col_idx] in visited:
                    return False
                
                visited.add(row[col_idx])

        # Check box index
        for i in range(3):
            for j in range(3):
                visited = set()
                for row_idx in range(i * 3, (i + 1) * 3):
                    for col_idx in range(j * 3, (j + 1) * 3):
                        num = board[row_idx][col_idx]
                        if num != '.' and num in visited:
                            return False

                        visited.add(num)

        return True

                





        