for i in range(1, 11):
    answer = 0
    count = int(input())
    heights = list(map(int, input().split()))
    while count:
        heights.sort(reverse=True)
        if heights[0] - heights[-1] <= 1:  # 평탄화 작업이 완료되었는지 확인
            answer = heights[0]-heights[-1]
            break
        heights[0] -= 1
        heights[-1] += 1
        answer = max(heights) - min(heights)
        count -= 1

    print("#{} {}".format(i, answer))