def minimumWeeklyInput(costs, weeks):
    n = len(costs)
    
    dp = [[float('inf')] * (n + 1) for _ in range(weeks + 1)]
    
    max_cost = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n):
        current_max = 0
        for j in range(i, n):
            current_max = max(current_max, costs[j])
            max_cost[i][j + 1] = current_max
    
    for i in range(1, n + 1):
        dp[1][i] = max_cost[0][i]
    
    for w in range(2, weeks + 1):
        for i in range(w, n + 1):
            for j in range(w - 1, i):
                dp[w][i] = min(dp[w][i], dp[w - 1][j] + max_cost[j][i])
    
    return dp[weeks][n]