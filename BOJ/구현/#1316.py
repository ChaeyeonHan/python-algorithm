n = int(input())
cnt = n

for i in range(n):
    word = input()  # 단어안에 불연속적으로 나타나는 문자가 있다면 그룹단어 X
    for j in range(0, len(word)-1):
        if word[j] != word[j+1]:
            if word[j] in word[j+1:]:  # 불연속적으로 겹치는 문자가 있는 경우
                cnt -= 1
                break
print(cnt)