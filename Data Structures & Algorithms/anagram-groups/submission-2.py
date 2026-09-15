class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Sort each string, group in hashmap
        # O(m * n * logn)
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
        