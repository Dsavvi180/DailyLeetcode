class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        transitions = [[0,3],[3,6],[6,9]]
        seenRow = set()
        seenCol = set()
        for i in range(rows):
            for x in board[i]:
                try:
                    z = int(x)
                    if z not in seenRow:
                        seenRow.add(z)
                    else:
                        return False
                except Exception as e:
                    pass
            seenRow.clear()
        for x in range(cols):
            for y in range(rows):
                try:
                    z = int(board[y][x])
                    if z not in seenCol:
                        seenCol.add(z)
                    else:
                        return False
                except Exception as e:
                    pass
            seenCol.clear()

        for j in transitions:
            currentRows = board[j[0]:j[1]]
            for i in transitions:

                currentMatrix = [currentRows[y][i[0]:i[1]] for y in range(len(currentRows))]
        
                seenSubMatrix = set()
                for index, row in enumerate(currentMatrix):
                    for x in row:
                        try:
                            x = int(x)
                            if x not in seenSubMatrix:
                                seenSubMatrix.add(x)
                            else:
                                return False
                        except Exception as e:
                            pass
        return True