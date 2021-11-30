N = int(input())
a = []
a = [0]*N

# a = []

for i in range(N):
    a[i] = int(input())

for i in range(N):
    min_index = i
    for j in range(i+1,N):
        if(a[min_index] > a[j]):
            min_index = j
    a[i], a[min_index] = a[min_index], a[i]

for i in range(N):
    print(a[i])
# print(a)