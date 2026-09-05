class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        cur, res = [], []
        def backtrack(char, open_cnt, close_cnt):
            cur.append(char)
            if char == "(":
                open_cnt += 1
            if char == ")":
                close_cnt += 1
            
            if close_cnt > open_cnt or open_cnt > n or close_cnt > n:
                cur.pop()
                return

            if len(cur) == 2 * n:
                res.append("".join(cur))
            else:
                backtrack("(", open_cnt, close_cnt)
                backtrack(")", open_cnt, close_cnt)

            cur.pop()

        backtrack("(", 0, 0)
        backtrack(")", 0, 0)
        return res

