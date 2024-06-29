def solution(number, k):
    stack = []
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    return ''.join(stack[:len(stack)-k])
    
    
    
#     answer = ''
#     num_list = list(map(int, number))
#     n = len(number)
#     f = 0
#     for i in range(n-k):  
#         if f+1 == n-k+1+i:
#             answer += ''.join(map(str, num_list[f:]))
#             break
#         else:
#             max_num = max(num_list[f:k+1+i])
#             max_index = num_list[f:k+1+i].index(max_num) + f
#             answer += str(max_num)
#             f = max_index + 1
#     return answer
    