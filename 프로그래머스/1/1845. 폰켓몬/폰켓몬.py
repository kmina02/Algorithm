def solution(nums):
    a = len(nums) // 2
    b = len(set(nums))
    if a < b:
        return a
    else:
        return b