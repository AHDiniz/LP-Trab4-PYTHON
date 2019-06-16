#!/usr/bin/python3

# LP-Trab4-PYTHON: Solving the point grouping problem with the leader algorithm
#
# Alan Herculano Diniz
#
# leader.py: leader algoritm implementation

import math



# Calculating the results of the leader algorithm
#
# Inputs: the list of points and the limit distance
#
# Output: the sse and the list of groups
def calculate_results(limit, points):
    groups = [[1]] # Creating the first group

    for i in range(1, len(points)): # Iterating through each point in the list

        leader = True

        for group in groups:

            if point_distance(points[group[0] - 1], points[i]) <= limit:

                if not (i + 1 in group):
                    group.append(i + 1)
                leader = False

        if leader:
            groups.append([i + 1])

    sse = calculate_sse(points, groups)
    return sse, groups



# Calculating the groups's sse
#
# Inputs: the list of points and the lists of grouped indeces
#
# Output: the groups' sse
def calculate_sse(points, groups):
    sse = 0

    for group in groups:
        center = center_of_mass(points, group)

        for index in group:
            sse = sse + point_distance(points[index - 1], center) ** 2

    return sse



# Calculating the distance between two points
#
# Inputs: the points that need to be compared
#
# Output: the distance between the given points
def point_distance(a, b):
    d = 0

    for i in range(len(a)):
        d = d + (a[i] - b[i]) ** 2

    return math.sqrt(d)



# Calculating the center of mass of a given point group
#
# Inputs: the list of points and the list of indeces of the points in the group
#
# Output: the center of mass of the group
def center_of_mass(points, group):
    center = []
    length = len(points[0])

    for i in range(length):
        center.append(0)

    for index in group:
        point = points[index - 1]
        for j in range(length):
            center[j] += point[j] / len(group)

    return center
