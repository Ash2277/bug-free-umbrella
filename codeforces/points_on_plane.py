import math


def place_chips(n):
    chips = [(0, 0)]  # start with a chip at the origin
    for i in range(1, n):
        min_cost = math.inf
        best_pos = None
        for x in range(-i, i+1):
            for y in range(-i, i+1):
                pos = (x, y)
                if pos not in chips:
                    # calculate cost of placing chip at this position
                    cost = max(abs(x)+abs(y),
                               [math.dist(pos, c) for c in chips])
                    if cost < min_cost:
                        # check if this position satisfies the distance constraint
                        if all(math.dist(pos, c) > 1 for c in chips):
                            min_cost = cost
                            best_pos = pos
        chips.append(best_pos)  # add the chip with the lowest cost
    return min([max(abs(x)+abs(y) for (x, y) in chips)], math.inf)


n = int(input())
l = []
for i in range(n):
    n = int(input("Enter the number of chips: "))
    min_cost = place_chips(n)
    l.append(min_cost)
for i in l:
    print(i)
