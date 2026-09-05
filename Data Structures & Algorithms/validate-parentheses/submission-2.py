class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "}": "{", "]": "["}
        st = []

        for char in s:
            if char in ["(", "[", "{"]:
                st.append(char)
            else:
                if len(st) == 0 or mapping[char] != st.pop():
                    return False 

        if len(st) > 0:
            return False
            
        return True
