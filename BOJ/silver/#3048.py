# n1, n2 = map(int, input().split())
# ant1 = list(str(input()))  # 개미순서 문자열로 입력
# ant2 = list(str(input()))
# time = int(input())
#
# ant1.reverse()  # 더하는 방향을 맞춰준다
# ant_sum = ant1 + ant2  # 개미 순서 합치기
#
# for i in range(time):
#     temp = []
#     for j in range(1, len(ant_sum)):
#         if ant_sum[j] in ant2:
#             if ant_sum[j-1] in ant1:  # 그룹1에 있는 개미이면 점프해 위치가 바뀌어야 하므로, temp배열에 인덱스값 저장
#                 temp.append(j)
#
#     for q in temp:  # 방향이 다른 두 개미 위치 바꿔주기
#         ant_sum[q] , ant_sum[q-1] = ant_sum[q-1], ant_sum[q]
#
# # print(ant_sum)
# result=''  # 리스트인 결과를 문자열로 출력하기 위한 과정
# for i in ant_sum:
#     result += i
# print(result)


# 배열로 작성해보기(참고)

N_number, M_number = map(int, input().split())
N = list(input())
N = N[::-1]  # 개미 방향을 맞춰주기 위해. 시작과 끝 인덱스 생략, 증가폭이 -1 => 리스트 반대로 뒤집기
M = list(input())
T = int(input())

ants = N+M
# 리스트에러 -> 40번째줄 k+1이 맨 마지막에서 문제가 생겼을수도??

for i in range(T):
    for ant in N:
        k = ants.index(ant) # ants안에서 해당 개미 인덱스 찾기
        if ants[k+1] in M:
            ants[k], ants[k+1] = ants[k+1], ants[k]  # 방향 다르면 자리 바꿔주기

result=''  # 리스트인 결과를 문자열로 출력하기 위한 과정
for i in ants:
    result += i
print(result)
# ,, 런타임 에러.....