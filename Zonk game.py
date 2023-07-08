from collections import Counter


def zonk_score(roll):
    counter = Counter(roll)
    total_score = 0

    # check for straight
    if set(roll) == set(range(1, 7)):
        return 1000

    # check for three pairs
    if sorted(counter.values()) == [2, 2, 2]:
        return 750

    for die, count in counter.items():
        if count >= 3:
            if die == 1:
                total_score += 1000 * (count // 3)
            else:
                total_score += 100 * die * (count // 3)
            counter[die] %= 3
        if die == 1:
            total_score += 100 * counter[die]
        if die == 5:
            total_score += 50 * counter[die]

    if total_score == 0:
        return "Zonk"

    return total_score
