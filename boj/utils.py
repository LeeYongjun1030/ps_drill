## combinations nCr
n = 4
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(n+1):
        if j == 0 or j == i:
            dp[i][j] = 1
            continue
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]


