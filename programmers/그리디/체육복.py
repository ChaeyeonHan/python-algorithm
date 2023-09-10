def solution(n, lost, reserve):
    n_lost = set(lost) - set(reserve)
    n_reserve = set(reserve) - set(lost)

    for i in n_lost:
        if i - 1 in n_reserve:
            n_reserve.remove(i - 1)
        elif i + 1 in n_reserve:
            n_reserve.remove(i + 1)
        else:
            n -= 1
    return n

    # for i in n_reserve:
    #     if i-1 in n_lost:
    #         n_lost.remove(i-1)
    #     elif i+1 in n_lost:
    #         n_lost.remove(i+1)
    # return n-len(n_lost)
