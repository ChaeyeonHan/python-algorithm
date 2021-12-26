N = int(input())
costs = list(map(int, input().split()))

max_costs = max(costs)

print(sum(costs)-max_costs)
