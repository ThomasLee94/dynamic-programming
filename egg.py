import math


def drop_egg(total_floors: int, total_eggs: int, memoized_list=None) -> int:
    """
        This function returns the minimum number of
        drops needed to guarentee that the pivotal
        floor (where the egg drops) is found.
    """

    # EXAMPLE MEMOIZED RESULTS TABLE:
    #            *FLOORS*
    #       *0* *1* *2* *3* *4*
    #     0  0   0   0   0   0
    #     1  0   1   2   3   4
    # E   2  0   1   2   2   3
    # G   3  0   1   2   2   3
    # G   4  0   1   2   2   3
    # S   5  0   1   2   2   3

    infinity = math.inf
    # === INIT MEMOIZED 2D LIST ===
    if memoized_list is None:
        memoized_list = list()
        for i in range(total_floors):
            memoized_list.append([])
            for j in range(total_eggs):
                memoized_list[i].append([])
                # infinity will be used for easy value comparison
                memoized_list[i][j] = infinity

    # recurisve calls
    # === BASE CASES ===
    # case: no floors or only 1 floor
    if total_floors in (0, 1):
        return total_floors
    # case: no eggs
    if total_eggs == 0:
        return total_eggs
    # case: only 1 floor
    if total_eggs == 1:
        return total_floors

    # if memoized values already exist
    if memoized_list:
        if memoized_list[total_floors - 1][total_eggs - 1] != infinity:
            return memoized_list[total_floors - 1][total_eggs - 1]

    # === FOR EVERY FLOOR ===
    for floor in range(1, total_floors + 1):
        # === DECISION TREE ===
        # case: egg breaks, minus current floor by 1 because we only consider
        # floors below it
        broken_egg = drop_egg(floor - 1, total_eggs - 1, memoized_list)
        # case: egg does not break, minus total floors by floor because we
        # only consider floors above it
        # * we have floors remaining, the difference between the total
        # * floors and the current floor
        egg = drop_egg(total_floors - floor, total_eggs, memoized_list)
        # maximum value from the 2 decisions
        worst_case_drops_num = max(broken_egg, egg)
        # +1 because because we want to account for the current floor
        worst_case_drops_num + 1

        # update memoization
        # print(f"total floors: {total_floors}")
        # print(f"total eggs: {total_eggs}")
        # print(memoized_list)
        memoized_list[floor - 1][total_eggs - 1] = min(
            worst_case_drops_num,
            memoized_list[total_floors - 1][total_eggs - 1],
        )

    return memoized_list[total_floors - 1][total_eggs - 1]


print(drop_egg(4, 2))
