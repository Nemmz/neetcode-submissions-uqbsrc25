class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        sqauresubgrid = collections.defaultdict(set) # key = (r/3,c/3)
        for r in range(9): # rows are 9 units long
            for c in range(9): # columns are 9 units long
                if board[r][c] == ".": # if the coordinates show a "." continue as it represents a blank space
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or 
                    board[r][c] in sqauresubgrid[(r//3, c//3)]): # check coordinates r,c are in the row and column and if they are in the subgrid.
                    return False
                cols[c].add(board[r][c]) 
                rows[r].add(board[r][c])
                sqauresubgrid[(r//3, c//3)].add(board[r][c]) # add to the hashmap the value located at r,c to the respective dictionaries.
        return True