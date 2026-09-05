class Solution:

    def encode(self, strs: List[str]) -> str:
        # Idea 1. Use a char outside 256 ascii char list
        # Idea 2. Use postion and char
        res = ""
        for i in range(len(strs)):
            res += f":: {strs[i]}\n"
        return res

    def decode(self, s: str) -> List[str]:
        strs = s.splitlines()
        res = []
        for i in range(len(strs)):
            temp = strs[i][3:]
            res.append(temp)

        print(res)
        return res
