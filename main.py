
import sys
import json
from itertools import combinations,permutations,product
from vrp_algorihtm import find_route
from inputdata import input_data

def write_file(route_list):
    with open('output.txt', 'w') as f:
        for item in route_list:
            f.write("%s\n" % item)
def main():
    write_file(find_route(input_data))

if __name__ == '__main__':
    main()
