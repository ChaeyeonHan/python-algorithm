import heapq

def solution(jobs):
    heap = []  # 소요시간 기준으로 최소힙을 만들어야함
    i = 0
    while i < len(jobs):
