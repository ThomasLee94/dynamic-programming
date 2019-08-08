def drop_egg(total_floors: int, floor_num: int, egg_num: int, drops_num=0) -> int:
    """
        This function returns the minimum number of
        drops needed to guarentee that the pivotal 
        floor (where the egg drops) is found.
    """

    # === BASE CASES ===
    # case: no floors
    if floor_num == 0:
        return floor_num
    # case: no eggs
    if egg_num == 0:
        return egg_num
    # case: only 1 floor
    if egg_num == 1:
        return total_floors
    # case: only 1 floor
    if floor_num == 1:
        return floor_num

    # === DECISION TREE ===
    # egg breaks
    broken_egg = drop_egg(total_floors, floor_num - 1, egg_num - 1, drops_num)
    # egg does not break
    egg = drop_egg(total_floors, floor_num + 1, egg_num, drops_num)

    drops_nums = max(broken_egg, egg)
    
    return drops_num