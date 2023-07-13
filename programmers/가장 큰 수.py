def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))  # 숫자를 문자열로 변환
    numbers.sort(key=lambda x: x * 3, reverse=True)

    # answer = answer.join(numbers)
    # return str(int(answer))
    return str(int("".join(numbers)))