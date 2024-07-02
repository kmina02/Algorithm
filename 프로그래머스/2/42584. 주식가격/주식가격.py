def solution(prices):
    answer = []
    for i in range(len(prices)):
        a = 0
        for j in range(i+1, len(prices)):
            a += 1
            if prices[i] > prices[j]: break
            # if prices[i] <= prices[j]:
            #     print(f'{prices[j]}는 {prices[i]}보다 크다.')
            # else:
            #     print(f'{prices[j]}는 {prices[i]}보다 크지 않다.')
            #     break
        answer.append(a)
    return answer