import math


def dfs_trace(initial,node_obj_list,final):
    alphanumeric_path = [initial]
    while True:

        if not alphanumeric_path:
            break

        cur_node = alphanumeric_path[len(alphanumeric_path) - 1]
        if cur_node == final:
            break

        available_in_nodes = False
        for nodeObj in node_obj_list:
            if nodeObj.root == cur_node:
                available_in_nodes = True
                nodeObj.visited = True
                next_node = ''
                neighbours = nodeObj.neighbours
                found_next_not_visited = False
                for an in neighbours:
                    if found_next_not_visited is True:
                        break
                    for nextObj in node_obj_list:
                        if nextObj.root == an and nextObj.visited is False:
                            next_node = nextObj.root
                            found_next_not_visited = True
                            break

                if next_node != '':
                    alphanumeric_path.append(next_node)
                else:
                    alphanumeric_path.pop()
                break

        if available_in_nodes is False:
            alphanumeric_path.pop()
            break

    return alphanumeric_path  # it will return empty if there is no path between initial and final locations


def dfs_length_calculate(alphanumeric_path, nodes_loc_obj_list):
    total_length = 0
    fromX = fromY = toX = toY = -1
    cityFrom = cityTo = ''
    for aPath in alphanumeric_path:
        for aLoc in nodes_loc_obj_list:
            if aLoc.root == aPath:
                if fromX == -1:
                    fromX = aLoc.locationX
                    fromY = aLoc.locationY
                    cityFrom = aPath
                    break
                else:
                    toX = aLoc.locationX
                    toY = aLoc.locationY
                    cityTo = aLoc.root
                    alphanumeric_path_length = math.sqrt(math.pow((toX - fromX), 2) + math.pow((toY - fromY), 2))
                    print(cityFrom + ' to ' + cityTo + ' length: ' + str(alphanumeric_path_length))
                    total_length += alphanumeric_path_length
                    fromX = toX
                    fromY = toY
                    cityFrom = cityTo
                    break
    return total_length


def reset_dfs_visit(node_obj_list, reset_lst):
    i = 0
    while i < len(node_obj_list):
        if i < len(reset_lst) and reset_lst[i]:
            node_obj_list[i].visited = True
        else:
            node_obj_list[i].visited = False
        i += 1
    return node_obj_list
