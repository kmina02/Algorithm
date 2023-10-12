goal = int(input())
team_one_score = 0
team_two_score = 0
team_one_time = 0
team_two_time = 0
time_score_dic = dict()
 
for _ in range(goal):
  team, win_time = input().split()
  m, s = map(int, win_time.split(":"))
    
  time_score_dic[m * 60 + s] = int(team)
 
for i in range(48 * 60):
    if i in time_score_dic:
      if time_score_dic[i] == 1:  
        team_one_score += 1
      else:
        team_two_score += 1
    
    if team_one_score > team_two_score:
      team_one_time += 1
    elif team_one_score < team_two_score:
      team_two_time += 1
    
team_one_m = team_one_time // 60
team_one_s = team_one_time % 60
 
team_two_m = team_two_time // 60
team_two_s = team_two_time % 60
 
print("{:02d}:{:02d}".format(team_one_m, team_one_s))
print("{:02d}:{:02d}".format(team_two_m, team_two_s))