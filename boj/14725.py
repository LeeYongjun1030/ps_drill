class Trie:
    def __init__(self, val=None):
        self.val = val
        self.children = {}

    def insert(self, seeds):
        trie = self
        for seed in seeds:
            if seed not in trie.children:
                trie.children[seed] = Trie()
            trie = trie.children[seed]

def dfs(node, num):
    for child in sorted(node.children.keys()):
        for _ in range(num):
            print('--', end='')
        print(child)
        dfs(node.children[child], num + 1)

n = int(input())
trie = Trie()
for _ in range(n):
    read = list(input().split())
    k, lst = int(read[0]), read[1:]
    trie.insert(lst)
dfs(trie, 0)
