from collections import defaultdict
from math import sqrt


def distance_between_coords(x1, y1, x2, y2):
    distance = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return distance


def name_coords(coords):
    coord_count = 0
    for coord in coords:
        coord_count += 1
        coord.append(coord_count)
    return coords


def graph(coords):
    coords = name_coords(coords)
    graph = defaultdict(list)
    edges = {}
    for current in coords:
        for comparer in coords:
            if comparer == current:
                continue
            else:
                weight = distance_between_coords(current[0], current[1],
                                                 comparer[0], comparer[1])
                graph[current[2]].append(comparer[2])
                edges[current[2], comparer[2]] = weight
    return coords, edges


def shortest_path(node_list, edges, start):
    neighbor = 0
    unvisited = []
    visited = []
    total_weight = 0
    current_node = start
    for node in node_list:
        if node[2] == start:
            visited.append(start)
        else:
            unvisited.append(node[2])
    while unvisited:
        for index, neighbor in enumerate(unvisited):
            if index == 0:
                current_weight = edges[start, neighbor]
                current_node = neighbor
            elif edges[start, neighbor] < current_weight:
                current_weight = edges[start, neighbor]
                current_node = neighbor
        total_weight += current_weight
        unvisited.remove(current_node)
        visited.append(current_node)
    return visited, total_weight


def get_optiomal_path():
    coords = [
                [1.7592675, 92.4836507], 
                [17.549836, 32.457398],
                [23.465896, 45],
                [25.195462, 37.462742],
                [42.925274, 63.234028]
            ]
    coords, edges = graph(coords)
    shortest_path(coords, edges, 3)
    shortest_path_taken = []
    shortest_path_weight = 0

    for index, node in enumerate(coords):
        path, weight = shortest_path(coords, edges, index + 1)
        print('--------------------------------------')
        print("Path", index + 1, "=", path)
        print("Weight =", weight)
        if index == 0:
            shortest_path_weight = weight
            shortest_path_taken = path
        elif weight < shortest_path_weight:
            shortest_path_weight = weight
            shortest_path_taken = path
    print('--------------------------------------')
    print("The weight of the path is:", shortest_path_weight)
    return shortest_path_taken


class Orders(object):
    """
    Implemented singleton class to handle orders and optimal path
    """
    def __init__(self):
        self.orders = {
            1: {
                'cust_name': 'foo',
                'address': '1016, huntingdon dr, san jose, CA 95129',
                'items': 'veg pizza'
            },
            2: {
                'cust_name': 'bar',
                'address': '1580, benton St, Sunnyvale, CA 95129',
                'items': 'veg pizza'
            },
            3: {
                'cust_name': 'user3',
                'address': '10239, E Estates Dr, cupertino, CA 95129',
                'items': 'veg pizza'
            },
            4: {
                'cust_name': 'user4',
                'address': '2112, huntingdon dr, san jose, ca 95129',
                'items': 'veg pizza'
            },
            5: {
                'cust_name': 'user5',
                'address': '1016, huntingdon dr, san jose, ca 95129',
                'items': 'veg pizza'
            }
        }

        self.path = get_optiomal_path()
        self.last_deliverd = -1

    def get_order(self):
        try:
            if not self.path or self.last_deliverd >= len(self.path) :
                return {'msg': 'No new/pending orders to deliver'}
            self.last_deliverd +=1
            print("ord no : ", self.last_deliverd)
            return self.orders[self.path[self.last_deliverd]]
        except Exception as ex:
            return {'msg': 'No new/pending orders to deliver'}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Orders, cls).__new__(cls)
            return cls.instance