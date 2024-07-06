def solution(n, times):
    start, end = 1, sorted(times)[-1] * n
    while start < end:
        mid = (start + end) // 2
        if sum([mid//t for t in times]) > n:
            end = mid - 1
        elif sum([mid//t for t in times]) < n:
            start = mid + 1
        else: 
            break
    return mid - sorted([mid%t for t in times])[0]