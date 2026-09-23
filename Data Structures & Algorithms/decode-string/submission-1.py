class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch.isdigit() and stack and stack[-1].isdigit():
                stack[-1] += ch
            elif ch.isalpha() and stack and stack[-1].isalpha():
                stack[-1] += ch
            elif ch == "]":
                print(stack)
                st = stack.pop()
                if stack[-1] == "[":
                    stack.pop()
                    k = stack.pop()
                    if stack and stack[-1].isalpha():
                        stack[-1] += (st * int(k))
                    else:
                        stack.append(st * int(k))
                else:
                    stack[-1] += st
                # repeated = st + k
                # if k.isdigit():
                #     repeated = st * int(k)
                # repeated = st * int(k)
                # if stack and stack[-1].isalpha:
                #     stack[-1] += repeated
                # else:
                #     stack.append(repeated)
            else:
                stack.append(ch)
        # print(stack)                                                                
        return stack[-1]