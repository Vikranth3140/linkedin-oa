def windFarms(premium, x, y):
    def weighted_median(coordinate, weights):
        sorted_items = sorted(zip(coordinate, weights))
        sorted_coord = [item[0] for item in sorted_items]
        sorted_weights = [item[1] for item in sorted_items]

        total_weight = sum(sorted_weights)
        cumulative_weight = 0
        for i in range(len(sorted_weights)):
            cumulative_weight += sorted_weights[i]
            if cumulative_weight >= total_weight / 2:
                return sorted_coord[i]
        return sorted_coord[-1]

    cx = weighted_median(x, premium)
    cy = weighted_median(y, premium)

    total_cost = 0
    for i in range(len(x)):
        distance = abs(x[i] - cx) + abs(y[i] - cy)
        total_cost += premium[i] * distance

    return total_cost