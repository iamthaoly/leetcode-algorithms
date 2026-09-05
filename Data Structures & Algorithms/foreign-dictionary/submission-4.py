class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Important: Note wrong syntax
        adj_list = dict()
        indegree = dict()
        processed = set()

        all_words = "".join(words)
        chars = set(all_words)
        for ch in chars:
            indegree[ch] = 0

        for i in range(len(words) - 1):
            a = words[i]
            b = words[i + 1]
            if a.startswith(b) and len(a) > len(b):
                return ""
            for j in range(min(len(a), len(b))):
                if a[j] != b[j]:
                    if (a[j], b[j]) not in processed:
                        if not adj_list.get(a[j]):
                            adj_list[a[j]] = [b[j]]
                        else:
                            adj_list[a[j]].append(b[j])
                        indegree[b[j]] += 1
                        processed.add((a[j], b[j]))
                    break

        res = ""
        queue = deque([c for c in indegree if indegree[c] == 0])
        # print(adj_list)
        # print(indegree)

        while (queue):
            c = queue.popleft()
            res += c
            for v in adj_list.get(c, []):
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        return res if len(res) == len(indegree) else ""

            