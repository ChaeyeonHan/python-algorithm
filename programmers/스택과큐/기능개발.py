def solution(progresses, speeds):
    result = []
    day, count = 0, 0  # 작업 일수 / 배포된 작업 갯수
    while progresses:
        if (progresses[0] + speeds[0] * day) >= 100:
            progresses.pop(0)  # 작업 리스트에서 삭제하고, 배포 개수 증가
            speeds.pop(0)
            count += 1
        else:
            if count > 0:  # 현재는 작업이 완료되지 않았지만 앞에서 배포작업이 있었다면
                result.append(count)
                count = 0
            day += 1

    result.append(count)  # 마지막 작업은 append 시키지 않고 while문을 빠져나왔기에
    return result
