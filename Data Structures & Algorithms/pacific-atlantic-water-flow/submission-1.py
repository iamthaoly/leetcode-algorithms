class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # input: heights[r][c] - height at coordinate (r, c)
        # pacific: top, left sides
        # atlantic: bottom, right sides
        # water flow:
        # - in 4 directions
        # - to neighbor with height <=
        # - to ocean (cell next to ocean)
        # output: cells flow to both ocean
        row = len(heights)
        col = len(heights[0])

        def dfs(i, j, prev):
            nonlocal p, a
            if not (0 <= i < row and 0 <= j < col and heights[i][j] >= prev):
                return
            
            if p:
                if (i, j) in pa:
                    return
                pa.add((i, j))
            if a:
                if (i, j) in at:
                    return
                at.add((i, j))
            
            val = heights[i][j]
            dfs(i, j + 1, val)
            dfs(i, j - 1, val)
            dfs(i + 1, j, val)
            dfs(i - 1, j, val)

        at, pa = set(), set()
        # visited = [[False for _ in range(col+1)] for _ in range(row+1)]
        # for i in range(row):
        #     for j in range(col):
        #         p = (i == 0 or j == 0) 
        #         a = (i == row - 1 or j == col - 1)
        #         if p or a:
        #             dfs(i, j, heights[i][j])
        p, a = True, False

        for c in range(col):
            p, a = True, False
            dfs(0, c, heights[0][c]) 
            a, p = True, False
            dfs(row - 1, c, heights[row - 1][c])   
        
        for r in range(row):
            p, a = True, False
            dfs(r, 0, heights[r][0])
            a, p = True, False
            dfs(r, col - 1, heights[r][col - 1])
        
        # & is set intersection (elements in both sets)
        # Practice this again, why nested loop not working
        common = at & pa
        res = [list(x) for x in common]
        return res

