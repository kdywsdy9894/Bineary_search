N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_list.sort()

def solution(N, M, N_list, M_list):
    for i in range(M):
        start = 0
        end = len(N_list)-1
        while start <= end:
            mid = (start + end)//2
            if M_list[i] == N_list[mid]:
                M_list[i] = 1
                start = end + 1
            elif M_list[i] > N_list[mid]:
                start = mid + 1
            else:
                end = mid - 1
        if M_list[i] != 1:
            M_list[i] = 0
    
    Mlist = list(map(lambda x: str(x), M_list))
    return " ".join(Mlist)

print(solution(N, M, N_list, M_list))

