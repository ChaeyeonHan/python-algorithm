'''

N = list(map(int, input()))
cnt = [0]*10  # 6이랑 9는 같이 카운트

for i in N:
    if i == 6 or i == 9:
        cnt[6] += 1
    else:
        cnt[i] += 1
# print(cnt)

max_cnt = max(cnt)
num = cnt.index(max_cnt)

if num == 6:
    print(max_cnt //2 + max_cnt %2)
    # print(int(max_cnt/2))
else:
    print(max_cnt)   # 최대가 6또는 9이면 2로 나눈 몫을 출력
=> 반례 : 6688 입력시 1이 나온다 -> max값을 찾을때 6을 8보다 먼저 찾아서 인덱스값으로 6이 들어가고,
         8은 무시되니까 !!!

'''



N = list(map(int, input()))
cnt = [0] * 9  # 6이랑 9는 같이 카운트
for i in N:
    if i == 6 or i == 9:
        cnt[6] += 1
    else:
        cnt[i] += 1

max_cnt = max(cnt)
num = cnt.index(max_cnt)

# result=[]
# for i in cnt:
#     if cnt[i] == max_cnt:
#         result.append(i)   # 6이랑 8 들어가게
result = [i for i in cnt if cnt[i] == max_cnt]


if len(result) == 1:
    if num == 6:
        print(max_cnt //2 + max_cnt %2)
    else:
        print(max_cnt)   # 최대가 6또는 9이면 2로 나눈 몫을 출력
else:
    print(max_cnt)


'''
# list comprehension ??
a= []
for i in range(10):
    a.append(i)

a = [i for i in range(10)]
'''

# word = input()
# ans = [0]*10
# for i in range(len(word)):
#     num = int(word[i])
#     if num == 6 or num == 9:  # 6과 9인경우 더 작은 인덱스값을 증가시켜준다
#         if ans[6] <= ans[9]:
#             ans[6] += 1
#         else:
#             ans[9] += 1
#     else:
#         ans[num] += 1
# print(max(ans))