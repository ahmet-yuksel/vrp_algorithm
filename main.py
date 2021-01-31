
import sys
import json
from itertools import combinations,permutations,product
from vrp_algorihtm import find_route
from inputdata import input_data
from sys import stdin

def write_file(route_list):
    with open('output.txt', 'w') as f:
        for route in route_list:
            del route['optimum_second']
            f.write("%s\n" % route)
def main():

    while True:
        input_optimum = input("Select optimal route(o) or total seconds(t) :").lower()
        if input_optimum == "o":
            optimum_flag = True
            break
        elif input_optimum == "t":
            optimum_flag = False
            break

    write_file(find_route(input_data, optimum_flag))

if __name__ == '__main__':
    main()
