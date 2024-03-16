import collections
import sys
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
graph = collections.defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[-a].append(b)
    graph[-b].append(a)
sccs=[]
id = 0
stack = []
degree = [-1 for _ in range(2*n+1)]

def set_id():
    global id
    id += 1
    return id

def dfs(node):
    degree[node] = set_id()
    stack.append(node)
    parent = degree[node]
    for next in graph[node]:
        if degree[next] == -1:
            parent = min(parent, dfs(next))
        elif next in stack:
            parent = min(parent, degree[next])
    if parent == degree[node]:
        scc = []
        while True:
            e = stack.pop()
            scc.append(e)
            if e == node: break
        sccs.append(scc)
    return parent

for i in range(-n, n+1):
    if i == 0: continue
    if degree[i] == -1:
        dfs(i)

possible = True
for scc in sccs:
    for i in scc:
        for j in scc:
            if i + j == 0:
                possible = False
if possible: print(1)
else: print(0)

if possible:
    result = [-1 for i in range(2*n+1)]
    lst = []
    for scc in sccs[::-1]:
        for e in scc:
            if result[e] != -1:
                continue
            result[e] = 0
            result[-e] = 1
    print(*result[1:n+1])