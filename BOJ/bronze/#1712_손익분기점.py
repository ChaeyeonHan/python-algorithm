fcost, mcost, sell_cost = map(int, input().split())
# split으로 입력받은 값을 공백을 기준으로 분리
# map과 함께 사용하여 split의 결과를 모두 int로 변환

if (mcost >= sell_cost):
    print(-1) # 손익분기점 존재하지 않음
else:
    print(fcost//(sell_cost-mcost)+1)
