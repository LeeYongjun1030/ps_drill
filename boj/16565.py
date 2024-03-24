import sys
sys.setrecursionlimit(10**5)
n = int(input())
if n < 4:
    print(0)
    sys.exit()

m=52
dp = [[0 for _ in range(m+1)] for _ in range(m+1)]
for i in range(1, m+1):
    for j in range(m+1):
        if j == 0 or j == i:
            dp[i][j] = 1
            continue
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

all=dp[52][n]

if n >= 40:
    print(all%10007)
    sys.exit()

max_iteration = 13
impossible = 0

def dfs(v, iteration, noc):
    global impossible
    if v == n:
        impossible += noc
        return
    elif iteration == max_iteration:
        return
    elif v >= n:
        return

    for i in range(4):
        dfs(v + i, iteration + 1, noc * dp[4][i])

dfs(0,0, 1)
print((all-impossible)%10007)