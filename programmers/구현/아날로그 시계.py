def solution(h1, m1, s1, h2, m2, s2):
    answer = 0

    # 시작/끝 시간을 초단위로 변경
    startTime = h1*3600 + m1*60 + s1
    endTime = h2*3600 + m2*60 + s2

    # 1초 뒤 시간부터 계산하기에, 00시와 12시는 포함된다면 여기서 계산
    if startTime == 0 * 3600 or startTime == 12 * 3600:
        answer += 1

    while startTime < endTime:
        # 현재 바늘들의 각도 계산
        hCurAngle = (startTime / 120) % 360
        mCurAngle = (startTime / 10) % 360
        sCurAngle = (startTime * 6) % 360

        # 1초 뒤의 바늘 각도를 구해서, 숫자 12 넘어갔는지 확인
        # 나눈 나머지가 0이면, 숫자 12를 넘어간 것.
        # if (startTime+1)/120 % 360 == 0:
        #     hNextAngle = 360
        # else:
        #     hNextAngle = (startTime+1)/120 % 360

        hNextAngle = 360 if (startTime+1)/120 % 360 == 0 else (startTime+1)/120 % 360
        mNextAngle = 360 if (startTime+1)/10 % 360 == 0 else (startTime+1)/10 % 360
        sNextAngle = 360 if (startTime+1)*6 % 360 == 0 else (startTime+1)*6 % 360

        if sCurAngle < hCurAngle and sNextAngle >= hNextAngle:
            answer += 1
        if sCurAngle < mCurAngle and sNextAngle >= mNextAngle:
            answer += 1
        if sNextAngle == mNextAngle == hNextAngle:
            answer -= 1
        startTime += 1
    return answer