def change(cash):

    if cash < 2:
        return None

    res = {
        'two': 0,
        'five': 0,
        'ten': 0
    }

    if cash >= 10:
        og_cash = cash
        res['ten'] = (cash//10)
        cash = cash % 10
        if og_cash % 10 > 0 and og_cash % 10 < 2:
            res['ten'] -= 1
            cash += 10


    if cash >= 5:
        og_cash = cash
        res['five'] = (cash//5)
        cash = cash % 5
        if (og_cash % 5) % 2 != 0:
            res['five'] -= 1
            cash += 5

    if cash % 2 == 0:
        res['two'] = cash // 2

    else:
        return None
    return res


print(change(8))