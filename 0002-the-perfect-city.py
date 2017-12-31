def isInt(number):
    return (number % 1 == 0)

def diffWithUpperInt(number):
    if (isInt(number)):
        return 0
    return number // 1 + 1 - number

def diffWithLowerInt(number):
    if (isInt(number)):
        return 0
    return number - number // 1

def getShortestPath(departure, destination):
    min_distance = [0, 0]
    if (departure[0] == destination[0]):
        return abs(departure[1] - destination[1])
    if (departure[1] == destination[1]):
        return abs(departure[0] - destination[0])

    for axis in range(0, 2):
        if (isInt(departure[axis]) or isInt(destination[axis]) or (departure[axis] // 1 != destination[axis] // 1)):
            min_distance[axis] = abs(departure[axis] - destination[axis])
        else:
            # In this case, for the current axis, the departure and the destination points are on the same block
            # We have to go to the next intersection for both the departure and the destination points in order to join them in a C-shape
            min_distance[axis] = min(diffWithUpperInt(departure[axis]) + diffWithUpperInt(destination[axis]), diffWithLowerInt(departure[axis]) + diffWithLowerInt(destination[axis]))
    return min_distance[0] + min_distance[1]

departure = [0.4, 1]
destination = [0.9, 3]
print(getShortestPath(departure, destination))
