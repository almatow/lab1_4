from typing import Iterable, Any


def common_count(*lists: Iterable[Any]) -> int:

    if not lists:
        return 0

    sets = [set(lst) for lst in lists]
    common = sets[0]
    for s in sets[1:]:
        common &= s
    return len(common)
