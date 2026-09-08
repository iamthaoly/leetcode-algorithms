class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Solution 1: Convert to decimal, add num, convert back to binary
        # Solution 2: Add binary directly
        # Todo: optimize res list
        remember = 0
        res = []
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0:
            da = db = 0
            if i >= 0:
                da = int(a[i])
            if j >= 0:
                db = int(b[j])
            cur = da ^ db ^ remember
            if (da + db + remember >= 2):
                remember = 1
            else:
                remember = 0

            res = [str(cur)] + res
            i -= 1
            j -= 1

        if remember > 0:
            res = ["1"] + res

        return "".join(res)            

                