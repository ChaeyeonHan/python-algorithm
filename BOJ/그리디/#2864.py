A, B = input().split()

max_A = A.replace('5', '6')
min_A = A.replace('6', '5')
max_B = B.replace('5', '6')
min_B = B.replace('6', '5')


print(int(min_A)+ int(min_B), int(max_A) + int(max_B))