nums = list(map(int, input().split()))
N = nums[0]
K = nums[1]
M = nums[2]

if K >= M:
    if K - M - 1 >= (N - K) + (M - 1):
        print((N - K) + (M - 1))
    else:
        print(K - M - 1)
elif M > K:
    if M - K - 1 >= (N - M) + (K - 1):
        print((N - M) + (K - 1))
    else:
        print(M - K - 1)
