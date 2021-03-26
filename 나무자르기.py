import sys

N, M = map(int, sys.stdin.readline().split())
H = list(map(int, sys.stdin.readline().split()))

def solution(M, H):
    lowest = 0
    highest = max(H)
    
    while lowest <= highest:
        mid = (lowest + highest)//2

        totalhigh = sum([H[i] - mid for i in range(N) if H[i] > mid])

        if totalhigh == M:
            return mid
        elif totalhigh > M:
            lowest = mid + 1
        else:
            highest = mid - 1
        
    if totalhigh > M:
        return mid
    else:
        return mid - 1
    
    

print(solution(M, H))