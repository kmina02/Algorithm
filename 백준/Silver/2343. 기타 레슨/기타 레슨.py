# 입력값 받기
n, m = map(int,input().split())
time = list(map(int,input().split()))

# 블루레이 크기의 최솟값을 start로, 최댓값을 end로 설정
start = max(time)
end = sum(time)

# 이분 탐색 진행
while start <= end:
    mid = (start + end) // 2 
		# 앞에서부터 차례대로 진행하기 위한 초기 설정
    total = 0 # 현재 블루레이의 길이
    count = 1 # 총 블루레이의 개수
		# 강의 리스트 앞에서부터 탐색
    for t in time:
				# 앞에서부터 누적으로 강의시간 더한 값이 mid보다 클 경우
        if total + t > mid:
            count += 1
            total = 0
        total += t 
		# 블루레이의 개수가 m보다 작거나 같을 때
    if count <= m:
        ans = mid
        end = mid - 1 # 더 작은 mid값이 있는지 탐색하기 위해
    else:
        start = mid + 1 # 블루레이의 개수가 m보다 큰 경우 start값을 키워서 덜 나눠지도록
    
print(ans)