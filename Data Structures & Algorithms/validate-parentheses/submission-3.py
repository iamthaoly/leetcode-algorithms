class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "}": "{", "]": "["}
        st = []

        for char in s:
            if char in mapping: # char is close parentheses
                if st and st[-1] == mapping[char]:
                    st.pop()
                else:
                    return False
            else:
                st.append(char)

        if st:
            return False
            
        return True
