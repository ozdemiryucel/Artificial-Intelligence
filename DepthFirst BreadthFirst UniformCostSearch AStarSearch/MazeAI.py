# Yucel Ozdemir
# 220201009
# This AI adds nodes to frontiers with the following line: Up, Down, Left, Right for all algorithms
import sys
from collections import deque
from enum import Enum
import functools
import copy
from typing import List
import random

# it is for printing side by side
printf = functools.partial(print, end="")


class Type(Enum):
    NORMAL = 1
    START = 2
    GOAL = 3
    WALL = 4


# x(row), y(column) are coordinates
# extra cost is extra cost
# types are NORMAL, START or GOAL
class Node:
    def __init__(self, extra_cost, type):
        self.x = None
        self.y = None
        self.extra_cost = extra_cost
        self.total_cost = 0
        self.type = type
        self.heuristic = None
        self.parent = None

    # Return possible actions. For example UD means directions of Up and Down is possible to go
    def get_actions(self):
        up = ""
        down = ""
        left = ""
        right = ""

        if self.type == Type.WALL:
            return "-"

        if (maze[self.x - 1][self.y].type == Type.NORMAL or maze[self.x - 1][
            self.y].type == Type.GOAL) and self.x - 1 >= 0:
            up = "U"

        try:
            if maze[self.x + 1][self.y].type == Type.NORMAL or maze[self.x + 1][self.y].type == Type.GOAL:
                down = "D"
        except:
            pass

        if (maze[self.x][self.y - 1].type == Type.NORMAL or maze[self.x][
            self.y - 1].type == Type.GOAL) and self.y - 1 >= 0:
            left = "L"

        try:
            if maze[self.x][self.y + 1].type == Type.NORMAL or maze[self.x][self.y + 1].type == Type.GOAL:
                right = "R"
        except:
            pass

        return up + down + left + right

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"


# This is a method for getting total cost of a node to sort frontiers
def getKey_for_Uniform_Cost_Search(node):
    return node.total_cost


# This is a method for getting total cost+heuristic of a node to sort frontiers
def getKey_for_A_Star_Search(node):
    return node.total_cost + node.heuristic


def breadth_first_search(labirent):
    frontier = deque()
    explored = []

    flag = False
    for i in labirent:  # Finds start node and adds to frontier
        for j in i:
            if j.type == Type.START:
                # node = j
                frontier.append(j)
                flag = True
                break
        if flag:
            break

    while True:

        if frontier.__len__() == 0:
            return "FAIL"

        # # To check frontiers
        # for i in frontier:
        #     printf(i , " - ")
        # print()

        node = frontier.popleft()
        explored.append(node)

        # # To check explored
        # for i in explored:
        #     printf(i , " - ")
        # print()

        actions = node.get_actions()

        # Check whether direction of Up is possible
        if "U" in actions:
            child = labirent[node.x - 1][node.y]

            if (child not in frontier) and (child not in explored):
                child.parent = node
                if child.type == Type.GOAL:
                    return child
                frontier.append(child)
            elif child in frontier:

                if frontier[frontier.index(child)].parent.parent != frontier[frontier.index(child)]:
                    frontier[frontier.index(child)].parent = node

        # Check whether direction of Down is possible
        if "D" in actions:
            child = labirent[node.x + 1][node.y]

            if (child not in frontier) and (child not in explored):
                child.parent = node
                if child.type == Type.GOAL:
                    return child
                frontier.append(child)
            elif child in frontier:
                if frontier[frontier.index(child)].parent.parent != frontier[frontier.index(child)]:
                    frontier[frontier.index(child)].parent = node

        # Check whether direction of Left is possible
        if "L" in actions:
            child = labirent[node.x][node.y - 1]

            if (child not in frontier) and (child not in explored):
                child.parent = node
                if child.type == Type.GOAL:
                    return child
                frontier.append(child)
            elif child in frontier:
                if frontier[frontier.index(child)].parent.parent != frontier[frontier.index(child)]:
                    frontier[frontier.index(child)].parent = node

        # Check whether direction of Right is possible
        if "R" in actions:
            child = labirent[node.x][node.y + 1]

            if (child not in frontier) and (child not in explored):
                child.parent = node
                if child.type == Type.GOAL:
                    return child
                frontier.append(child)
            elif child in frontier:
                if frontier[frontier.index(child)].parent.parent != frontier[frontier.index(child)]:
                    frontier[frontier.index(child)].parent = node


def depth_first_search(labirent):
    stack = []
    explored = []

    flag = False
    for i in labirent:
        for j in i:
            if j.type == Type.START:
                stack.append(j)
                flag = True
                break
        if flag:
            break

    while True:
        if stack.__len__() == 0:
            return "FAIL"

        # # To check stacks
        # for i in stack:
        #     printf(i , " - ")
        # print()

        node = stack.pop()
        explored.append(node)

        # # To check explored
        # for i in explored:
        #     printf(i , " - ")
        # print()

        actions = node.get_actions()

        if "U" in actions:
            child = labirent[node.x - 1][node.y]

            if (child not in stack) and (child not in explored):
                child.parent = node
                if child.type == Type.GOAL:
                    # TODO
                    # return explored yaparsan explored a goal u ekle
                    return child
                stack.append(child)
            elif child in stack:
                if stack[stack.index(child)].parent.parent != stack[stack.index(child)]:
                    stack[stack.index(child)].parent = node
            # elif child in explored:
            #     if explored[explored.index(child)].parent.parent != explored[stack.index(child)]:
            #     explored[explored.index(child)].parent = node

        if "D" in actions:
            child = labirent[node.x + 1][node.y]

            if (child not in stack) and (child not in explored):
                child.parent = node
                if child.type == Type.GOAL:
                    return child
                stack.append(child)
            elif child in stack:
                if stack[stack.index(child)].parent.parent != stack[stack.index(child)]:
                    stack[stack.index(child)].parent = node

        if "L" in actions:
            child = labirent[node.x][node.y - 1]

            if (child not in stack) and (child not in explored):
                child.parent = node
                if child.type == Type.GOAL:
                    return child
                stack.append(child)
            elif child in stack:
                if stack[stack.index(child)].parent.parent != stack[stack.index(child)]:
                    stack[stack.index(child)].parent = node

        if "R" in actions:
            child = labirent[node.x][node.y + 1]

            if (child not in stack) and (child not in explored):
                child.parent = node
                if child.type == Type.GOAL:
                    return child
                stack.append(child)
            elif child in stack:
                if stack[stack.index(child)].parent.parent != stack[stack.index(child)]:
                    stack[stack.index(child)].parent = node


def uniform_cost_search(labirent, type_of_Uniform_Cost_Search):
    frontier = []
    explored = []

    # Changes extra costs to 0 for not taking extra move points
    if type_of_Uniform_Cost_Search == 1:
        for i in range(len(labirent)):
            for j in range(len(labirent[i])):
                labirent[i][j].extra_cost = 0

    flag = False
    for i in labirent:  # Finds start node and adds to frontier
        for j in i:
            if j.type == Type.START:
                frontier.append(j)
                flag = True
                break
        if flag:
            break

    while True:

        if frontier.__len__() == 0:
            return "FAIL"

        frontier.sort(key=getKey_for_Uniform_Cost_Search)  # Sort according to extra_cost

        # # To check frontiers
        # for i in frontier:
        #     printf(i, " - ")
        # print()

        node = frontier[0]

        if node.type == Type.GOAL:
            return node

        frontier.remove(frontier[0])
        explored.append(node)

        # # To check explored
        # for i in explored:
        #     printf(i , " - ")
        # print()

        actions = node.get_actions()

        if "U" in actions:
            child = labirent[node.x - 1][node.y]

            if (child not in frontier) and (child not in explored):
                child.parent = node

                child.total_cost = child.extra_cost + child.parent.total_cost + 1

                frontier.append(child)
            else:
                is_there_in_frontier = False
                for i in frontier:
                    if i.__str__() == child.__str__():
                        is_there_in_frontier = True
                        index = frontier.index(i)
                        break

                if is_there_in_frontier:
                    if child.total_cost < frontier[index].total_cost:
                        child.parent = node

                        child.total_cost = child.extra_cost + child.parent.total_cost + 1

                        frontier[index] = child

        if "D" in actions:
            child = labirent[node.x + 1][node.y]

            if (child not in frontier) and (child not in explored):
                child.parent = node

                child.total_cost = child.extra_cost + child.parent.total_cost + 1

                frontier.append(child)
            else:
                is_there_in_frontier = False
                for i in frontier:
                    if i.__str__() == child.__str__():
                        is_there_in_frontier = True
                        index = frontier.index(i)
                        break

                if is_there_in_frontier:
                    # TODO
                    # printf(frontier[index].extra_cost - child.extra_cost, " , ")
                    if child.total_cost < frontier[index].total_cost:
                        child.parent = node

                        child.total_cost = child.extra_cost + child.parent.total_cost + 1

                        frontier[index] = child

        if "L" in actions:
            child = labirent[node.x][node.y - 1]

            if (child not in frontier) and (child not in explored):
                child.parent = node

                child.total_cost = child.extra_cost + child.parent.total_cost + 1

                frontier.append(child)
            else:
                is_there_in_frontier = False
                for i in frontier:
                    if i.__str__() == child.__str__():
                        is_there_in_frontier = True
                        index = frontier.index(i)
                        break

                if is_there_in_frontier:

                    if child.total_cost < frontier[index].total_cost:
                        child.parent = node

                        child.total_cost = child.extra_cost + child.parent.total_cost + 1

                        frontier[index] = child

        if "R" in actions:
            child = labirent[node.x][node.y + 1]

            if (child not in frontier) and (child not in explored):
                child.parent = node

                child.total_cost = child.extra_cost + child.parent.total_cost + 1

                frontier.append(child)
            else:

                is_there_in_frontier = False
                for i in frontier:
                    if i.__str__() == child.__str__():
                        is_there_in_frontier = True
                        index = frontier.index(i)
                        break

                if is_there_in_frontier:

                    if child.total_cost < frontier[index].total_cost:
                        child.parent = node

                        child.total_cost = child.extra_cost + child.parent.total_cost + 1

                        frontier[index] = child


def a_star_search(labirent, type_of_A_Star_Search):
    frontier = []
    explored = []

    # Set heuristics for A Star Search to be admissible
    if type_of_A_Star_Search == "admissible":
        for i in range(len(labirent)):
            for j in range(len(labirent[i])):
                if labirent[i][j].type == Type.GOAL:
                    labirent[i][j].heuristic = 0
                else:
                    labirent[i][j].heuristic = 1

    # Set heuristics for A Star Search to be inadmissible
    elif type_of_A_Star_Search == "inadmissible":
        for i in range(len(labirent)):
            for j in range(len(labirent[i])):
                if labirent[i][j].type == Type.GOAL:
                    labirent[i][j].heuristic = 0
                else:
                    labirent[i][j].heuristic = random.randint(1000, sys.maxsize)

    flag = False
    for i in labirent:  # Finds start node and adds to frontier
        for j in i:
            if j.type == Type.START:
                frontier.append(j)
                flag = True
                break
        if flag:
            break

    while True:
        if frontier.__len__() == 0:
            return "FAIL"

        frontier.sort(key=getKey_for_A_Star_Search)  # sort according to extra_cost

        # # To check frontiers
        # for i in frontier:
        #     printf(i, " - ")
        # print()

        node = frontier[0]

        if node.type == Type.GOAL:
            return node

        frontier.remove(frontier[0])
        explored.append(node)

        # # To check explored
        # for i in explored:
        #     printf(i , " - ")
        # print()

        actions = node.get_actions()

        if "U" in actions:
            child = labirent[node.x - 1][node.y]

            if (child not in frontier) and (child not in explored):

                child.parent = node

                child.total_cost = child.extra_cost + child.parent.total_cost + 1

                frontier.append(child)
            else:
                is_there_in_frontier = False
                for i in frontier:
                    if i.__str__() == child.__str__():
                        is_there_in_frontier = True
                        index = frontier.index(i)
                        break

                if is_there_in_frontier:
                    if child.total_cost < frontier[index].total_cost:
                        child.parent = node

                        child.total_cost = child.extra_cost + child.parent.total_cost + 1

                        frontier[index] = child

        if "D" in actions:
            child = labirent[node.x + 1][node.y]

            if (child not in frontier) and (child not in explored):
                child.parent = node

                child.total_cost = child.extra_cost + child.parent.total_cost + 1
                # print(child.total_cost)
                frontier.append(child)

            else:
                is_there_in_frontier = False
                for i in frontier:
                    if i.__str__() == child.__str__():
                        is_there_in_frontier = True
                        index = frontier.index(i)
                        break

                # printf(frontier[index].extra_cost-child.extra_cost , " , ")

                if is_there_in_frontier:
                    if child.total_cost < frontier[index].total_cost:
                        child.parent = node

                        child.total_cost = child.extra_cost + child.parent.total_cost + 1

                        frontier[index] = child

        if "L" in actions:
            child = labirent[node.x][node.y - 1]

            if (child not in frontier) and (child not in explored):
                child.parent = node

                child.total_cost = child.extra_cost + child.parent.total_cost + 1

                frontier.append(child)
            else:
                is_there_in_frontier = False
                for i in frontier:
                    if i.__str__() == child.__str__():
                        is_there_in_frontier = True
                        index = frontier.index(i)
                        break

                if is_there_in_frontier:

                    if child.total_cost < frontier[index].total_cost:
                        child.parent = node

                        child.total_cost = child.extra_cost + child.parent.total_cost + 1

                        frontier[index] = child

        if "R" in actions:
            child = labirent[node.x][node.y + 1]

            if (child not in frontier) and (child not in explored):
                child.parent = node

                child.total_cost = child.extra_cost + child.parent.total_cost + 1

                frontier.append(child)
            else:

                is_there_in_frontier = False
                for i in frontier:
                    if i.__str__() == child.__str__():
                        is_there_in_frontier = True
                        index = frontier.index(i)
                        break

                if is_there_in_frontier:

                    if child.total_cost < frontier[index].total_cost:
                        child.parent = node

                        child.total_cost = child.extra_cost + child.parent.total_cost + 1

                        frontier[index] = child




def write_path_using_goal_state(node):
    if node == "FAIL":
        print(node)
        return
    lst = []
    while True:
        if node.type == Type.START:
            lst.append(node)
            break
        p = node.parent
        lst.append(node)
        node = p

    lst.reverse()
    for i in lst:
        if i.type == Type.GOAL:
            printf(i.__str__())
        else:
            printf(i.__str__(), "-> ")
    print()


def draw_maze():
    print("\n------MAZE------")
    for i in maze:
        for j in i:
            if j.type == Type.START:
                printf("S", "\t")
            elif j.type == Type.NORMAL:
                printf(".", "\t")
            elif j.type == Type.WALL:
                printf("X", "\t")
            elif j.type == Type.GOAL:
                printf("G", "\t")
        print()


# Initialize maze
# Node(extra_cost, Type)
maze: List[List[Node]] = \
    [[Node(0, Type.START),  Node(0, Type.NORMAL), Node(1, Type.NORMAL), Node(0, Type.NORMAL), Node(1, Type.NORMAL)],
     [Node(-1, Type.WALL),  Node(-1, Type.WALL),  Node(2, Type.NORMAL), Node(1, Type.NORMAL), Node(2, Type.NORMAL)],
     [Node(2, Type.NORMAL), Node(-1, Type.WALL),  Node(3, Type.NORMAL), Node(0, Type.NORMAL), Node(-1, Type.WALL)],
     [Node(0, Type.NORMAL), Node(2, Type.NORMAL), Node(1, Type.NORMAL), Node(1, Type.NORMAL), Node(-1, Type.WALL)],
     [Node(1, Type.NORMAL), Node(0, Type.NORMAL), Node(3, Type.GOAL),   Node(1, Type.NORMAL), Node(-1, Type.WALL)]]

# Set coordinates of nodes
for x in range(len(maze)):
    for y in range(len(maze[x])):
        maze[x][y].x = x
        maze[x][y].y = y


def main():

    draw_maze()

    print("\nBreadth First Search:")
    goal_state_of_BFS = breadth_first_search(copy.deepcopy(maze))
    write_path_using_goal_state(goal_state_of_BFS)

    print("\n\nDepth First Search:")
    goal_state_of_DFS = depth_first_search(copy.deepcopy(maze))
    write_path_using_goal_state(goal_state_of_DFS)

    print("\n\nUniform Cost Search 1 (without extra cost):")
    goal_state_of_UCS_1 = uniform_cost_search(copy.deepcopy(maze), 1)
    if goal_state_of_UCS_1 != "FAIL":
        print("Total cost:", goal_state_of_UCS_1.total_cost)
    write_path_using_goal_state(goal_state_of_UCS_1)

    print("\n\nUniform Cost Search 2 (with extra cost):")
    goal_state_of_UCS_2 = uniform_cost_search(copy.deepcopy(maze), 2)
    if goal_state_of_UCS_2 != "FAIL":
        print("Total cost:", goal_state_of_UCS_2.total_cost)
    write_path_using_goal_state(goal_state_of_UCS_2)

    goal_state_of_A_Star_Search = a_star_search(copy.deepcopy(maze), "inadmissible")
    print(
        "\n\nA* Search 1 (inadmissible) (It might be rarely optimal due to random heuristics. If it is so, please run again):")
    if goal_state_of_A_Star_Search != "FAIL":
        print("Total cost:", goal_state_of_A_Star_Search.total_cost)
    write_path_using_goal_state(goal_state_of_A_Star_Search)

    goal_state_of_A_Star_Search = a_star_search(copy.deepcopy(maze), "admissible")
    print("\n\nA* Search 2 (admissible):")
    if goal_state_of_A_Star_Search != "FAIL":
        print("Total cost:", goal_state_of_A_Star_Search.total_cost)
    write_path_using_goal_state(goal_state_of_A_Star_Search)

    # for i in maze:
    #     print()
    #     for j in i:
    #         printf(j.extra_cost , "\t")
    # print()

    # for i in maze:
    #     print()
    #     for j in i:
    #         printf(j.get_actions() , "\t")
    # print()
    # print()


if __name__ == "__main__":
    main()
