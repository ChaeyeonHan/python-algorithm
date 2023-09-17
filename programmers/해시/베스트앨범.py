# 가장 많이 재생된 장르에서 많이 재생된 노래 2곡 수록(재생횟수가 같다면 고유번호가 낮은노래 먼저)
# 고유번호도 필요하기에, dict에 함께 저장해준다!
def solution(genres, plays):  # 장르, 재생 횟수
    answer = []
    play_times = {}  # 장르 : (고유번호, 재생횟수)
    total = {}  # 장르별 재생횟수 저장
    for i in range(len(genres)):
        if genres[i] in play_times:
            play_times[genres[i]] += [(i, plays[i])]
            total[genres[i]] += plays[i]
        else:
            play_times[genres[i]] = [(i, plays[i])]
            total[genres[i]] = plays[i]
    # print(play_times)  # {'classic': [(0, 500), (2, 150), (3, 800)], 'pop': [(1, 600), (4, 2500)]}
    # print(total)  # {'classic': 1450, 'pop': 3100}
    total = sorted(total.items(), key=lambda x: -x[1])  # value를 기준으로 내림차순 정렬

    for key in total:
        playlist = play_times[key[0]]  # play_times[pop]  pop장르 가져와서
        playlist = sorted(playlist, key=lambda x: -x[1])

        for i in range(len(playlist)):
            if i == 2:
                break
            else:
                answer.append(playlist[i][0])  # idx 넣어주기
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))