#!/usr/bin/python3

# LP-Trab4-PYTHON: Solving the point grouping problem with the leader algorithm
#
# Alan Herculano Diniz
#
# main.py: program's entry point

import sys
import reader
import leader

# Getting the command line arguments with the input filepaths:
if (len(sys.argv) == 1):
    points_file = "entrada.txt"
    dist_file = "distancia.txt"
else: # Avoiding null filepaths
    points_file = sys.argv[1]
    dist_file = sys.argv[2]

# Reading the input files:
points, dist = reader.read_files(points_file, dist_file)

# Calculating the algorithm results:
sse, groups = leader.calculate_results(dist, points)

# Printing the algorithm results:
reader.print_results(sse, groups)
