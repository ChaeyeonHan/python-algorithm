# number = "1231234"
# number_list = [int(i) for i in number]
# k = 3
# temp = []
# for i in range(k):
#     temp.append((i, int(number[i])))
# temp.sort(key=lambda x:-x[1])
# first = temp[0][1]  # 첫번째 자리수 지정
# for i in range(temp[0][0]):  # temp[0][0]값인 2개 삭제
#     number_list.pop(0)
#     # print(number_list)  # [3, 1, 2, 3, 4]

# 스택을 활용한 풀이
def solution(number, k):
    stack = []

    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    # k가 남아있다면 남은 k개의 숫자는 뒤에서부터 제거
    # if k > 0:
    # print(stack)
    stack = stack[:-k]
    # print(stack)
    return "".join(stack)

print(solution("1231234", 3))