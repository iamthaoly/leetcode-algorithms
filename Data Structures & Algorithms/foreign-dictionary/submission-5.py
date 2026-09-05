class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Solution 2: Topo sort (Optimized)
        # - Remove processed
        # - Init both indegree and adj_list
        # - Optimize string concatenation
        # - str += c # Time complexity: O(n^2) Each += creates a new string
        # Important: Note wrong syntax
        chars = set("".join(words))
        adj_list = {ch: set() for ch in chars}
        indegree = {c: 0 for c in adj_list}

        for i in range(len(words) - 1):
            a = words[i]
            b = words[i + 1]
            if a.startswith(b) and len(a) > len(b):
                return ""
            for j in range(min(len(a), len(b))):
                if a[j] != b[j]:
                    if b[j] not in adj_list[a[j]]:
                        adj_list[a[j]].add(b[j])
                        indegree[b[j]] += 1
                    break

        res = []
        queue = deque([c for c in indegree if indegree[c] == 0])

        while (queue):
            c = queue.popleft()
            res.append(c)
            for v in adj_list[c]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        return "".join(res) if len(res) == len(indegree) else ""

            