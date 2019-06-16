#!/usr/bin/python3

# LP-Trab4-PYTHON: Solving the point grouping problem with the leader algorithm
#
# Alan Herculano Diniz
#
# reader.py: file manipulation functionalities



# Reading the given input files:
#
# Inputs: the points filepath and the distance filepath
#
# Output: the list of points and the limit distance
def read_files(points_loc, dist_loc):

    # Opening the points file:
    points_file = open(points_loc)

    # Opening the distance file:
    dist_file = open(dist_loc)

    # Reading the distance file
    dist = float(dist_file.read())

    # Reading the points file
    lines = points_file.readlines()

    # Creating the points list:
    points = []
    for i in range(0, len(lines)):
        words = lines[i].strip().split()
        points.append([])
        for j in range(0, len(words)):
            points[i].append(float(words[j]))

    return points, dist



# Printing the output files
#
# Inputs: the sse value and the list of groups
def print_results(sse, groups):

    # Opening/Creating the sse file:
    result = open("result.txt", "w+")

    # Opening/Creating the groups file:
    exitFile = open("saida.txt", "w+")

    # Writing the sse in result.txt:
    sseStr = "%.4f\n" % (sse)
    result.write(sseStr)

    for group in groups:
        for index in group:
            exitFile.write(str(index))
            exitFile.write(" ")
        exitFile.write("\n")

    return
