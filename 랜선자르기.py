K, N = map(int, input().split())
K_len = [int(input()) for i in range(K)]

def solution(K, N):
    low_len = 1
    high_len = max(K_len)

    while low_len <= high_len:
        mid_len = (low_len + high_len)//2
        total = sum([K_len[j]//mid_len for j in range(K) if K_len[j]>=mid_len])
        if total >= N:
            low_len = mid_len + 1
        else:
            high_len = mid_len - 1
        
    if total < N:
        return mid_len - 1
    else:
        return mid_len

print(solution(K, N))

