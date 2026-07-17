class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c, target_index):
            if target_index==len(word):
                return True

            if r<0 or r>ROWS-1 or c< 0 or c> COLS-1 or (r,c) in visited or board[r][c]!=word[target_index]:
                return False

            visited.add((r,c))

            target_index+=1
                
            found = (dfs(r-1,c, target_index) or #left
                    dfs(r,c+1, target_index)  or # up
                    dfs(r+1,c, target_index)  or #right
                    dfs(r,c-1, target_index)) # down

            visited.remove((r,c))
            
            return found
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        return False
        
            



        