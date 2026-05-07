class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenRows = [set() for _ in range(9)]
        seenCols = [set() for _ in range(9)]
        seenBoxes = [[set() for _ in range(3)] for _ in range(3)]

        # seenBoxes [
        #     [set(), set(), set()], 
        #     [set(), set(), set()],
        #     [set(), set(), set()]
        # ]

        # checks for duplicates in each row
        for row in range(len(board)):
            for col_i in range(len(board[row])):
                n = board[row][col_i]
                if n != '.':
                    if n in seenRows[row]:
                        return False
                    seenRows[row].add(n)
                    
                    if n in seenCols[col_i]:
                        return False
                    seenCols[col_i].add(n)

                    vals = self.getBox(row, col_i)
                    boxRow = vals[0] 
                    boxCol = vals[1]

                    if n in seenBoxes[boxRow][boxCol]:
                        return False
                    seenBoxes[boxRow][boxCol].add(n)
        return True

    def getBox(self, row: int, col: int):
        if 0 <= int(row) <= 2:
            boxRow = 0
        elif 3 <= int(row) <= 5:
            boxRow = 1
        else:
            boxRow = 2

        if 0 <= int(col) <= 2:
            colBox = 0
        elif 3 <= int(col) <= 5:
            colBox = 1
        else:
            colBox = 2

        return [boxRow, colBox]

        # print(f"seenRows FALSE hit, i: {i}, n: {n} ")

        # print(f"seenCols FALSE hit, i: {i}, n: {n} ")

        # print('seenCols', seenCols)
        # print('i', i)