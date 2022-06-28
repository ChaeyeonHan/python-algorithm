import sys
crob_alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

words = sys.stdin.readline().rstrip()  # 문자열로 받았음

for i in crob_alp:
    words = words.replace(i, "*")
    # 길이를 구해주면 되니까 replace함수를 사용해 *로 바꿔주고 단어 길이를 출력해준다
    # print(words)

print(len(words))