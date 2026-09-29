class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def build_adj(word):
            chars = list(word)
            for i in range(len(chars)):
                c, chars[i] = chars[i], "*"
                w = "".join(chars)
                adj_list[w].add(word)
                variation[word].append(w)
                chars[i] = c
        
        if endWord not in wordList:
            return 0       
        # Build adj list
        adj_list = defaultdict(set)
        variation = defaultdict(list)

        build_adj(beginWord)
        for word in wordList:
            build_adj(word)
        
        # print(variation)
        visited = set(beginWord)
        visited_v = set()
        q = deque([])
        for v in variation[beginWord]:
            for neighbor in adj_list[v]:
                if neighbor != beginWord:
                    q.append(neighbor)
                    visited.add(neighbor)
            adj_list[v].clear()
        
        count = 1
        while q:
            size = len(q)
            count += 1
            for _ in range(size):
                word = q.popleft()
                if word == endWord:
                    return count
                for v in variation[word]:
                    for nb in adj_list[v]:
                        if nb not in visited:
                            q.append(nb)
                            visited.add(nb)
                    adj_list[v].clear()

        return 0


