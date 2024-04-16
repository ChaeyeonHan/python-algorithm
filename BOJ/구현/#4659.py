import sys

vowel = ['a', 'e', 'i', 'o', 'u']
while True:
    test = input().rstrip()
    if test == "end":
        break
    repeat = 0
    flag = True
    for i in test:
        if i in vowel:
            repeat += 1  # 모음 갯수 카운트
    if repeat == 0:
        flag = False
    for i in range(len(test)-2):  # 모음3개, 자음3개 이상 체크
        if test[i] in vowel and test[i+1] in vowel and test[i+2] in vowel:
            flag = False
        elif test[i] not in vowel and test[i+1] not in vowel and test[i+2] not in vowel:
            flag = False
    for i in range(len(test)-1):
        if test[i] == test[i+1]:
            if test[i] == 'e' or test[i] =='o':
                continue
            else:
                flag = False
    if flag == True:
        print(f"<{test}> is acceptable.")
    else:
        print(f"<{test}> is not acceptable.")