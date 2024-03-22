n = int(input())
nums = list(map(int, input().split()))
nums.sort()
answer = 0
large = 1000000007

fsum = [0 for _ in range(n)] # fowrard prefix sum
bsum = [0 for _ in range(n)] # backward prefix sum
fsum[0]=nums[0]
bsum[0]=nums[-1]
for i in range(1, n):
    fsum[i] = fsum[i-1] + nums[i]
    bsum[i] = bsum[i-1] + nums[-i-1]

dsum = [0 for _ in range(n)] # difference fsum and bsum(sorted reverse)
for i in range(n):
    dsum[-i-1] = bsum[i] - fsum[i]


powers = [0 for _ in range(n+1)] # array for powers of two

def daq(num):  # divide and conquer
    if powers[num] != 0:
        return powers[num]
    if num <= 1:
        powers[num] = 2 ** num
        return powers[num]

    half = num // 2
    if num % 2 == 0:
        d = daq(half) ** 2
        powers[num] = d % large
        return d
    else:
        d = daq(half)*daq(half+1)
        powers[num] = d % large
        return d

for k in range(n):
    daq(k)

answer = 0
for i in range(1, n):
    answer += powers[i-1] * dsum[i]
print(answer % large)
