def bolling_game(ary):
    ary.extend([0, 0])
    tmp = -1
    total = 0
    for i in range(len(ary)):
        score = ary[i]
        if score == 10 and tmp == -1:
            total += score + ary[i+1] + ary[i+2]
        elif tmp >= 0:
            tmp += score
            if tmp == 10:
                total += tmp + ary[i+1]
            else:
                total += tmp
            tmp = -1
        else:
            tmp = score
    return total
