def checkStraightLine(coordinates):
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]

    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        # Calculate the slope between (x1, y1) and (x, y)
        if (y - y1) * (x2 - x1) != (x - x1) * (y2 - y1):
            return False

    return True

# Test case
coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
print(checkStraightLine(coordinates))
