class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        left = []
        right = []
        for a in asteroids:
            if a < 0:
                while right and abs(a) > right[-1]:
                    right.pop()
                if right and abs(a) == right[-1]:
                    right.pop()
                elif not right:
                    left.append(a)
            else:
                right.append(a)
                
        return left + right
    def asteroidCollision2(self, asteroids: List[int]) -> List[int]:
        s = []
        for a in asteroids:
            if not s or (s[-1] * a > 0) or (s[-1] < 0 and a > 0):
                s.append(a)
                continue
            should_append = True
            while s and s[-1] > 0 and a < 0 and abs(a) >= abs(s[-1]):
                if abs(a) == abs(s[-1]):
                    s.pop()
                    should_append = False
                    break
                s.pop()
            if should_append:
                s.append(a)
                # if not s or abs(a) == abs(s[-1]):
                #     break
            # if not s:
            #     s.append(a)
                # continue
            # elif abs(a) == abs(s[-1]):
            #     s.pop()
        return list(s)
