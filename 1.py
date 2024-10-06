def calculateTotalRegion(heights):
    n = len(heights)
    
    # Arrays to store how far we can go left and right
    left = [0] * n
    right = [0] * n
    
    # Calculate left array
    for i in range(n):
        if i == 0 or heights[i] > heights[i - 1]:
            left[i] = 1
        else:
            left[i] = left[i - 1] + 1
    
    # Calculate right array
    for i in range(n - 1, -1, -1):
        if i == n - 1 or heights[i] > heights[i + 1]:
            right[i] = 1
        else:
            right[i] = right[i + 1] + 1
    
    # Calculate the total sum of all regions
    total_sum = 0
    for i in range(n):
        total_sum += left[i] + right[i] - 1
    
    return total_sum