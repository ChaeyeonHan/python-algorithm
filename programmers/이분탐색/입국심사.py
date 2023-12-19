def solution(n, times):
    start, end = 0, max(times) * n
    # 시간을 탐색해서 딱 적절하게 심사할 수 있는 시간을 찾아준다
    while start <= end:
        mid = (start + end) // 2
        people = 0  # 심사한 사람 수
        for t in times:
            people += mid // t
            if people >= n:
                break
        if people >= n:  # 딱 n명 심사, 남는 시간이 있는지 확인하기
            answer = mid
            end = mid - 1
        else:  # 인원수 미달.
            start = mid + 1

    return answer