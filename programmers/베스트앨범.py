def solution(genres, plays):
    # 장르 리스트 -> 딕셔너리로 변환
    # 딕셔너리로 각 장르마다 횟수 카운트 해서 많이 들은 장르별로 내림차순 정렬리스트 만들기
    # 장르별로 최대 두개씩 인덱스값 넣기
    answer = []
    play_times = {}
    total = {}
    for i in range(len(genres)):
        key = genres[i]
        if key in play_times:
            play_times[key] += [(i, plays[i])]  # (인덱스, 재생횟수)
            total[key] += plays[i]
        else:  # 없으면
            play_times[key] = [(i, plays[i])]
            total[key] = plays[i]
    # print(play_times)  # {'classic': [(0, 500), (2, 150), (3, 800)], 'pop': [(1, 600), (4, 2500)]}

    # value를 기준으로 내림차순 정렬, (key, value)형태로 반환
    # print(total)  # {'classic': 1450, 'pop': 3100}
    total = sorted(total.items(), key=lambda x: -x[1])  # [('pop', 3100), ('classic', 1450)]

    for key in total:  # 장르별로 2곡만 수록
        # print(key)  # ('pop', 3100)
        playlist = play_times[key[0]]  # key[0] = pop
        playlist = sorted(playlist, key=lambda x: -x[1])
        # print(playlist)  # [(1, 600), (4, 2500)]

        for i in range(len(playlist)):
            if i == 2:
                break
            else:
                answer.append(playlist[i][0])
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))