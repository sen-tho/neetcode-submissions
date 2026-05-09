class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = collections.defaultdict(set)
        colMap = collections.defaultdict(set)
        box = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                val = board[row][col]

                if val == '.':
                    continue
                
                if val in rowMap[row]:
                    return False
                
                if val in colMap[col]:
                    return False

                if val in box[(row // 3, col // 3)]:
                    return False

                rowMap[row].add(val)
                colMap[col].add(val)
                box[(row // 3, col // 3)].add(val)
        return True
                

