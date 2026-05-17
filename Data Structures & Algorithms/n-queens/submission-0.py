class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        col = set()
        pd = set()
        nd = set()

        result = []

        board = [ ["."]*n for i in range(n)]

        def back_tracking(r):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)

            for c in range(n):

                if c in col or r+c in pd or r-c in nd:
                    continue

                col.add(c)
                pd.add(r+c)
                nd.add(r-c)
                board[r][c] = "Q"
                back_tracking(r+1)


                col.remove(c)
                pd.remove(r+c)
                nd.remove(r-c)
                board[r][c] = "."

        back_tracking(0)
        return result