import sys
from NodeCls import *
from LocationCls import *
import itertools
from DFSTracer import *

file1 = open("./connections.txt", "r")
connections = file1.readlines()
file2 = open("./locations.txt", "r")
locations = file2.readlines()

nodes_loc_obj_list = []
available_nodes = []
for aLocation in locations:
    aLocationList = aLocation.split()
    if aLocationList[0] != 'END':
        available_nodes.append(aLocationList[0])
        nodes_loc_obj_list.append(LocationCLs(aLocationList))

node_obj_list = []
for aConnection in connections:
    aConnectionList = aConnection.split()
    if aConnectionList[0] != 'END':
        node_obj_list.append(NodeCls(aConnectionList))

print('#### DFS by Gautam Saini and Shilpi FNU ####')
print('List of cities:')
print(available_nodes)

initial_Exists = False
initial = ''
while initial_Exists is False:
    initial = input("Enter Initial location: ")
    if initial in available_nodes:
        initial_Exists = True
    else:
        print('City is not available in list. Enter city from list: ')

finale_exists = False
final = ''
while finale_exists is False:
    final = input("Enter Final location: ")
    if final in available_nodes:
        finale_exists = True
    else:
        print('City is not available in list. Enter city from list.')

if initial == final:
    sys.exit("Start and end city are same. Try again.")

print('_____________________________________________________________')
alphanumeric_path = dfs_trace(initial, node_obj_list, final)
if not alphanumeric_path:
    print("No alphanumeric DFS path found")
else:
    print('DFS path tracing alphanumeric order: ' + str(alphanumeric_path))
    total_alphanumeric_path = dfs_length_calculate(alphanumeric_path, nodes_loc_obj_list)
    print('Total alphanumeric DFS path length: ' + str(total_alphanumeric_path))
print('_____________________________________________________________')
print("###### Tracing alternative 4 DFS path in total available combination:  " + str(pow(2, (len(available_nodes)))))
efficient_counter = 1
path_counter = 0
alternative_path_lst = []
if alphanumeric_path:
    alternative_path_lst = [alphanumeric_path]
while efficient_counter < len(available_nodes):
    if path_counter == 4:
        break
    efficient_counter += 1
    all_2n_combinations = list(itertools.product([0, 1], repeat=efficient_counter))

    for aCombination in all_2n_combinations:
        node_obj_list = reset_dfs_visit(node_obj_list, aCombination)
        alt_path = dfs_trace(initial, node_obj_list, final)
        if alt_path and alt_path not in alternative_path_lst:
            alternative_path_lst.append(alt_path)
            print('Alternative Path ' + str(path_counter + 1) + ': ' + str(alt_path))
            total_length = dfs_length_calculate(alt_path, nodes_loc_obj_list)
            print('Path length: ' + str(total_length))
            print('_____')
            path_counter = path_counter+1
        if path_counter == 4:
            break

if int(len(alternative_path_lst)) == 1:
    print("No alternative path found between " + initial + ' and ' + final)

