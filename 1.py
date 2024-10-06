def calculateTotalRegion(heights):
    n = len(heights)
    
    left = [0] * n
    right = [0] * n
    
    stack = []
    for i in range(n):
        while stack and heights[stack[-1]] <= heights[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1] + 1
        else:
            left[i] = 0
        stack.append(i)
    
    stack.clear()
    
    for i in range(n-1, -1, -1):
        while stack and heights[stack[-1]] <= heights[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1] - 1
        else:
            right[i] = n - 1
        stack.append(i)
    
    total_sum = 0
    for i in range(n):
        region_length = (right[i] - left[i] + 1)
        total_sum += region_length
    
    return total_sum