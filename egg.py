def drop_egg(total_floors: int, num_eggs: int) -> int:
    """
        This function returns the minimum number of
        drops needed to guarentee that the pivotal
        floor (where the egg drops) is found.
    """

    # === BASE CASES ===
    # case: no floors or only 1 floor
    if total_floors in (0, 1):
        return total_floors
    # case: no eggs
    if num_eggs == 0:
        return num_eggs
    # case: only 1 floor
    if num_eggs == 1:
        return total_floors

    # for every floor
    for floor in total_floors:
        # === DECISION TREE ===
        # egg breaks
        broken_egg = drop_egg(total_floors - 1, num_eggs - 1)
        # egg does not break
        egg = drop_egg(total_floors + 1, num_eggs)

        drops_num = max(broken_egg, egg)

        return drops_num


print(drop_egg(100, 2))
