class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Solution 2: Dictionary (optimized)
        res = defaultdict(list)
        for word in strs:
            chars = [0] * 26
            a = ord('a')
            for ch in word:
                chars[ord(ch) - a] += 1
            # key = " ".join(str(freq) for freq in chars)
            res[tuple(chars)].append(word)
        # print(res)
        vals = list(res.values())
        return vals

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        # Solution 1: Sort
        # Sort each string, group in hashmap
        # O(m * n * logn)
        # Solution 2: Dictionary
        res = defaultdict(list)
        for word in strs:
            chars = [0] * 27
            a = ord('a')
            for ch in word:
                chars[ord(ch) - a] += 1
            key = " ".join(str(freq) for freq in chars)
            res[key].append(word)
        # print(res)
        vals = list(res.values())
        return vals
        