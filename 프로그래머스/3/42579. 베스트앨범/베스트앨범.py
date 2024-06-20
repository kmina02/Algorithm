def solution(genres, plays):
    music_count = {}
    answer = []
    for i in range(len(genres)):
        if genres[i] not in music_count:
            music_count[genres[i]] = 0
        music_count[genres[i]] += plays[i]
    genres_sorted = sorted(music_count.items(), key = lambda x: x[1], reverse = True)

    # 장르별 고유 번호와 재생 횟수를 담은 딕셔너리 music 생성
    music = {}
    for genre in genres_sorted:
        music[genre[0]] = []
    for i in range(len(genres)):
        g, p = genres[i], plays[i]
        music[g].append([i, p])

    # 장르 내에서 많이 재생된 노래를 먼저 수록
    answer.extend([x[0] for music_info in music.values() for x in sorted(music_info, key=lambda x: (-x[1], x[0]))[:2]])


    return answer