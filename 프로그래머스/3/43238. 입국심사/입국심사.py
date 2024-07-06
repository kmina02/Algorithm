def solution(n, times):
    k = sorted(times)[0]
    min = k * n
    start, end = 1, 1e19
    while start <= end:
        mid = (start + end) // 2
        if sum([mid//t for t in times]) > n:
            end = mid - 1
        elif sum([mid//t for t in times]) < n:
            start = mid + 1
        else: 
            break
    # while True:
    #     mid -= 1
    #     if sum([mid//t for t in times]) < n:
    #         break
    return mid - sorted([mid%t for t in times])[0]