from copy import deepcopy


def solution(key, lock):
    # get dimensions
    n = len(lock)
    m = len(key)
    result_size = n + (2 * m)

    # create result board
    result = [[0] * result_size for _ in range(m)] + \
             [[0] * m + lock_row + [0] * m for lock_row in lock] + \
             [[0] * result_size for _ in range(m)]

    # rotate keys
    key_90 = list(zip(*reversed(key)))
    key_180 = list(zip(*reversed(key_90)))
    key_270 = list(zip(*reversed(key_180)))

    # check by 4 dir
    for key in [key, key_90, key_180, key_270]:
        for dx in range(result_size - m):
            for dy in range(result_size - m):
                # init result
                _result = deepcopy(result)

                # add key to _result
                for i in range(m):
                    for j in range(m):
                        _result[dx + i][dy + j] += key[i][j]

                # check lock of _result
                unlocked = True
                for i in range(n):
                    for j in range(n):
                        if _result[m + i][m + j] != 1:
                            unlocked = False
                if unlocked:
                    return True
    return False
