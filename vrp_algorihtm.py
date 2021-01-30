
import sys
import json
from itertools import combinations,permutations


#Calc  possible vehicle order matchings
def calc_possible_vehicle_order(data):
    route_comb =[]
    vehicle_ids = [vhc["id"] for vhc in data["vehicles"]]
    order_ids = [order["id"] for order in data["jobs"]]
    vhc_lst = {}
    k = 0
    #START Vehicle Combination [1,2,3],[1,2],[1,3],[2,3],[1],[2],[3]
    for vehicle_comb_index in range(len(vehicle_ids)):
        comb = combinations(vehicle_ids, vehicle_comb_index+1)

        for i in list(comb):
            vhc_lst[str(k)] = list(i)
            k += 1

    # END Vehicle Combination

#START distribute orders by vehicle list
#return possible vehicle-order matchings list
    for item in vhc_lst:
        comb_orders_list = comb_orders_by_vehicle(order_ids, vhc_lst[item])
        if isinstance(comb_orders_list, list):
            for col in comb_orders_list:
                route_comb.append(col)
        else:
            route_comb.append(comb_orders_list)

    return route_comb
#END distribute orders by vehicle list

#START distribute orders by vehicle list combinations
#
def comb_orders_by_vehicle(order_loc,vhc_comp_list):
    route_lst2 = {1: [], 2: [], 3: []}
    route_lst4=[]
    if len(vhc_comp_list) == 1:
        route_lst2[vhc_comp_list[0]] = order_loc
        return route_lst2
    elif len(vhc_comp_list) > 1:
        for vhc in vhc_comp_list:
            for vehicle_perm_index in range(len(order_loc)):
                perm = combinations(order_loc, vehicle_perm_index+1)
                for i in list(perm):
                    route_lst = {1: [], 2: [], 3: []}
                    list(i).sort()
                    route_lst[vhc] = list(i)
                    route_lst2 = comb_orders_by_vehicle(list(set(order_loc) - set(list(i))),list(set(vhc_comp_list)-set([vhc])))
                    if isinstance(route_lst2, list):
                        for item in route_lst2:
                            route_lst3 = {x: route_lst.get(x, 0) + item.get(x, 0)
                                          for x in set(route_lst).union(item)}

                            route_lst4.append(route_lst3)
                    else:
                        route_lst3 = {x: route_lst.get(x, 0) + route_lst2.get(x, 0)
                                      for x in set(route_lst).union(route_lst2)}

                        route_lst4.append(route_lst3)

        return route_lst4
#END distribute orders by vehicle list

#START calc minimum  permutations of route (vehicle-order matching)
#route :{1:[1,2],2:[5,6],3:[3,4,7]}
# 1:[1,2] = 3000 sec
# 1:[2,1] = 2000 sec *
# 2:[5,6] = 1000 sec *
# 2:[6,5] = 2500 sec
# 3:[3,4,7] = 1300 sec
# 3:[4,3,7] = 1200 sec
# 3:[7,3,4] = 1900 sec
# 3:[4,7,3] = 1000 sec *
# 3:[3,7,4] = 1700 sec
# 3:[7,4,3] = 4000 sec
#return {1:[2,1],2:[5,6],3:[4,7,3], 'Total_second':4000}
def calc_min_duration(data,route):

    min_seconds = sys.maxsize
    max_seconds = 0
    min_vhc_id=0
    min_order_list=[]
    route_lst2 = {1: [], 2: [], 3: [],"Total_second":0}

    for rt in route:
        perm = permutations(route[rt])
        min_seconds = sys.maxsize
        for i in list(perm):

            vhc_id,order_list,total_second = calc_duration(data, rt, list(i))
            if min_seconds>=total_second:
                min_seconds=total_second
                min_vhc_id=vhc_id
                min_order_list=order_list

        route_lst2[min_vhc_id] = min_order_list
        max_seconds = max_seconds + min_seconds
        route_lst2["Total_second"] = max_seconds

    return route_lst2
#END calc minimum  permutations of route (vehicle-order matchin)

#START Calc Duration route given the matrix
#2:[5,6]   vehicle id 2-> order id 5->order id 6-> vehicle id 2
def calc_duration(data,vhc_id,order_list):

    if len(order_list) == 0:
        return vhc_id, order_list, 0

    vehicles = {input["id"]: input["start_index"] for input in data["vehicles"]}
    orders = {input["id"]: input["location_index"] for input in data["jobs"]}

    #first step vehicle to first order duration
    total_seconds = data["matrix"][vehicles[vhc_id]][orders[order_list[0]]]
    for ordr in range(len(order_list)-1):
        total_seconds += data["matrix"][orders[order_list[ordr]]][orders[order_list[ordr+1]]]
    #last step last order to vehicle
    total_seconds += data["matrix"][orders[order_list[len(order_list)-1]]][vehicles[vhc_id]]
    return vhc_id, order_list, total_seconds


def find_route(data):

    all_possible_vehicle_order = calc_possible_vehicle_order(data)

    #remove duplicate sorted route
    all_possbile_routes= {json.dumps(v): v for v in all_possible_vehicle_order}.values()


    route_list =[]
    # calc min route duration and route_list
    for route in all_possbile_routes:
        route_list.append(calc_min_duration(data, route))

    # sort route list and print first route
    route_list.sort(key=myFunc)
    return route_list

#sort function
def myFunc(e):
    return e['Total_second']

