class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(min(strs))
        res = []
        # print(min_len)
        for i in range(min_len):
            if not strs[0]:
                return "".join(res)
            prefix = strs[0][i]
            
            for j in range(1, len(strs)):
                if not (strs[j] and strs[j][i] == prefix):
                    return "".join(res)
            res.append(prefix)


        return "".join(res)

