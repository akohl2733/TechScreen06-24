def closest_to_zero(lst):
    if len(lst) == 0:
        return None
    res = []
    for i in lst:
        if len(res) < 1:
            res.append(i)
            continue
        if abs(res[0]) > abs(i):
            res.pop(0)
            res.append(i)
        elif abs(res[0]) == abs(i):
            res.append(max(res[0], i))
            res.pop(0)
        else:
            pass
    return res[0]


print(closest_to_zero([-2147283647]))