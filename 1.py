def calculateTotalRegion(heights):
    n = len(heights)
    
    # Arrays to store the farthest left and right boundary for each student
    left = [0] * n
    right = [0] * n
    
    # Monotonic stack for the left boundaries
    stack = []
    for i in range(n):
        # Find the farthest left where height is greater than or equal to current height
        while stack and heights[stack[-1]] < heights[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1] + 1
        else:
            left[i] = 0  # No taller element on the left
        stack.append(i)
    
    # Clear the stack for the right boundary calculation
    stack.clear()
    
    # Monotonic stack for the right boundaries
    for i in range(n-1, -1, -1):
        # Find the farthest right where height is greater than or equal to current height
        while stack and heights[stack[-1]] < heights[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1] - 1
        else:
            right[i] = n - 1  # No taller element on the right
        stack.append(i)
    
    # Calculate the total sum of all regions
    total_sum = 0
    for i in range(n):
        region_length = right[i] - left[i] + 1
        total_sum += region_length
    
    return total_sum