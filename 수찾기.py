N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()

def solution(x, lst):
    
    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = (start+end)//2
        if x == lst[mid]:
            return 1
        elif x > lst[mid]:
            start = mid + 1
        else:
            end = mid - 1
        
    return 0

for i in range(len(B)):
    print(solution(B[i], A))