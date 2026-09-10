class Solution:
    class DSU:
        def __init__(self, n):
            self.parent = list(range(n))
        
        def find(self, x):
            # while x != self.parent[x]:
            #     x = self.parent[x]
            # return x

            # Optimize 1: Path compression
            if x != self.parent[x]:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, a, b):
            root_a = self.find(a)
            root_b = self.find(b)
            if root_a != root_b:
                self.parent[root_b] = root_a

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = self.DSU(len(accounts))
        emails = {}
        for i, acc in enumerate(accounts):
            name, em = acc[0], acc[1:]
            for email in em:
                if email not in emails:
                    emails[email] = i
                else:
                    dsu.union(i, emails[email])

        # Group emails by root
        root_emails = defaultdict(set)
        for i, acc in enumerate(accounts):
            em = acc[1:]
            root = dsu.find(i)
            # Add all emails from the current acc to root's
            root_emails[root].update(em)

        res = []
        for root, email_set in root_emails.items():
            name = accounts[root][0]
            res.append([name] + sorted(email_set))
        return res

        

