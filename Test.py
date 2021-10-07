visited_nodes = []
been_to = []
been_to.clear()
import math
import queue
queue = queue.Queue()
visited_nodes = []
actions_to_take = ["N", "E", "S", "W"]


def expand(maze, node):
    tempNode = []
    for direction in actions_to_take:
        if(direction == "N"):
            new_node = (node.pos[0]-1, node.pos[1])
            if(maze[new_node] != "X"):
                node1 = Node(pos=new_node, parent=node, action="N", cost=1)
                tempNode.append(node1)
        if(direction == "E"):
            new_node = (node.pos[0], node.pos[1]+1)
            if(maze[new_node] != "X"):
                node2 = Node(pos=new_node, parent=node, action="E", cost=1)
                tempNode.append(node2)
        if(direction == "S"):
            new_node = (node.pos[0]+1, node.pos[1])
            if(maze[new_node] != "X"):
                node3 = Node(pos=new_node, parent=node, action="S", cost=1)
                tempNode.append(node3)
        if(direction == "W"):
            new_node = (node.pos[0], node.pos[1]-1)
            if(maze[new_node] != "X"):
                node4 = Node(pos = new_node , parent = node, action = "W", cost = 1)
                tempNode.append(node4)
    for x in tempNode:
        if((maze[x.pos]) == "X"):
            print((maze[x.pos]))
            tempNode.remove(x)
    return tempNode




def manhattanSearch(cur_node):
    goal = find_pos(maze,"G")
    cur_cordinate = [cur_node.pos[0],cur_node.pos[1]]
    goal_cordinate = [goal[0],goal[1]] 
    return sum(abs(val1-val2) for val1,val2 in zip(cur_cordinate,goal_cordinate))



def BestFirstSearchGreedy(maze):
    visited_nodes.clear()
    node = Node(pos = (find_pos(maze, what = "S")), parent = None, action = None, cost = 0)
    visited_nodes.append(node.pos)
    queue.put(node)  
    if(maze[node.pos] == "G"):
        return node.pos
    else:
        while queue:
            minim = math.inf
            check = queue.get()
            print(check)
            if(check.pos == find_pos(maze, what = "G")):
                path = check.get_path_from_root()
                path1 = [n.pos for n in path]
                sum1 = sum([n.cost for n in path])
                print("Positions:", [n.pos for n in path])
                print("Actions:", [n.action for n in path])
                print("This took: " + str(sum1) + " steps")
                # show_maze(maze,path1)
                return check.pos
            else:
                neighbors = expand(maze,check)
                for x in neighbors:
                    result = manhattanSearch(x)
                    if result < minim:
                        minim = result
                        if(x.pos not in visited_nodes):
                            visited_nodes.append(x.pos)
                            queue.put(x)

    


def AStart(maze):
    been_to.clear()
    node = Node(pos = (find_pos(maze, what = "S")), parent = None, action = None, cost = 0)
    been_to.append(node.pos)
    queue.put(node)  
    if(maze[node.pos] == "G"):
        return node.pos
    else:
        while queue:
            minim = math.inf
            check = queue.get()
            print(check)
            if(check.pos == find_pos(maze, what = "G")):
                path = check.get_path_from_root()
                path1 = [n.pos for n in path]
                print("Positions:", [n.pos for n in path])
                print("Actions:", [n.action for n in path])
                sum1 = sum([n.cost for n in path])
                print("This took: " + str(sum1) + " steps")
                # show_maze(maze,path1)
                return check.pos
            neighbors = expand(maze,check)
            for x in neighbors:
                temppath = x.get_path_from_root()
                distance = sum([n.cost for n in temppath])
                result = manhattanSearch(x) + distance
                if result < minim:
                    minim = result
                    if(x.pos not in been_to):
                        been_to.append(x.pos)
                        queue.put(x)