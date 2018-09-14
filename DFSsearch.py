import puzzle
import sys
import queue
import copy
import time



def display(lists):
    print(" ------------------- ")
    print(" | ", lists[0][0], " | ", lists[0][1], " | ", lists[0][2], " | ")
    print(" ------------------- ")
    print(" | ", lists[1][0], " | ", lists[1][1], " | ", lists[1][2], " | ")
    print(" ------------------- ")
    print(" | ", lists[2][0], " | ", lists[2][1], " | ", lists[2][2], " | ")
    print(" -------------------")

def check_validity_operate(lists, position, prev_pos ):
    i=lists.zero[0]
    j=lists.zero[1]
    if position == "up" and i > 0 and prev_pos != 'd':
        return 1
    elif position == "down" and i < 2 and prev_pos != 'u':
        return 1
    elif position == "left" and j > 0 and prev_pos != 'r':
        return 1
    elif position == "right" and j < 2 and prev_pos != 'l':
        return 1
    else:
        return 0

def check_visited(lists,visited_nodes):
    if lists in visited_nodes.values():
        return 1
    else:
        return 0

def left(lists, level, visited_nodes):
    global m
    i=lists.zero[0]
    j=lists.zero[1]
    if j>0:
        print("\nFrom Level", level)
        lists.printPuzzle()
        print("Moving left")
        lists.doMove("L")
        level=level+1
        print("To Level",level)
        lists.printPuzzle()

        if check_visited(lists.puzzle,visited_nodes)==0 and level<limitation:
            if lists.checkPuzzle()!=True:
                m=m+1
                visited_nodes[m]=copy.deepcopy(lists.puzzle)
                getlist=copy.deepcopy(lists)

                lists=copy.deepcopy(getlist)
                left(lists, level, visited_nodes)

                lists=copy.deepcopy(getlist)
                up(lists, level, visited_nodes)

                lists=copy.deepcopy(getlist)
                down(lists, level, visited_nodes)
            else:
                print("Final State reached")
                print("Total nummber of nodes generated",m)
                sys.exit()
        else:
            print("\nBack to the previous level")

def right(lists, level, visited_nodes):
    global m
    i=lists.zero[0]
    j=lists.zero[1]
    if j<2:
        print("\nFrom Level", level)
        lists.printPuzzle()
        print("Moving Right")
        lists.doMove("R")
        level=level+1
        print("To Level",level)
        lists.printPuzzle()

        if check_visited(lists.puzzle,visited_nodes)==0 and level<limitation:
            if lists.checkPuzzle()!=True:
                m=m+1
                visited_nodes[m]=copy.deepcopy(lists.puzzle)
                getlist=copy.deepcopy(lists)

                lists=copy.deepcopy(getlist)
                right(lists, level, visited_nodes)

                lists=copy.deepcopy(getlist)
                up(lists, level, visited_nodes)

                lists=copy.deepcopy(getlist)
                down(lists, level, visited_nodes)
            else:
                print("Final State reached")
                print("Total nummber of nodes generated",m)
                sys.exit()
        else:
            print("Back to the previous level")

def up(lists, level, visited_nodes):
    global m
    i=lists.zero[0]
    j=lists.zero[1]
    if i>0:
        print("\nFrom Level", level)
        lists.printPuzzle()
        print("Moving Up")
        lists.doMove("U")
        level=level+1
        print("To Level",level)
        lists.printPuzzle()

        if check_visited(lists.puzzle,visited_nodes)==0 and level<limitation:
            if lists.checkPuzzle()!=True:
                m=m+1
                visited_nodes[m]=copy.deepcopy(lists.puzzle)
                getlist=copy.deepcopy(lists)

                lists=copy.deepcopy(getlist)
                up(lists, level, visited_nodes)

                lists=copy.deepcopy(getlist)
                left(lists, level, visited_nodes)

                lists=copy.deepcopy(getlist)
                right(lists, level, visited_nodes)
            else:
                print("\nFinal State reached")
                print("Total nummber of nodes generated",m)
                sys.exit()

        else:
            print("Back to the previous level")

def down(lists, level, visited_nodes):
    global m
    i=lists.zero[0]
    j=lists.zero[1]
    if i<2:
        print("\nFrom Level", level)
        lists.printPuzzle()
        print("Moving Down")
        lists.doMove("D")
        level=level+1
        print("To Level",level)
        lists.printPuzzle()

        if check_visited(lists.puzzle,visited_nodes)==0 and level<limitation:
            if lists.checkPuzzle()!=True:
                m=m+1
                visited_nodes[m]=copy.deepcopy(lists.puzzle)
                getlist=copy.deepcopy(lists)

                lists=copy.deepcopy(getlist)
                down(lists, level, visited_nodes)

                lists=copy.deepcopy(getlist)
                left(lists, level, visited_nodes)

                lists=copy.deepcopy(getlist)
                right(lists, level, visited_nodes)

                print("all children searched over")
            else:
                print("Final State reached")
                print("Total nummber of nodes generated",m)
                sys.exit()
        else:
            print("Back to the previous level")

global limitation
limitation=int(10)

matrix = puzzle.TilePuzzle(int(3))
goal = copy.deepcopy(matrix.puzzle)

matrix.permute(int(3))  # the complexity of the initial state
initial = copy.deepcopy(matrix.puzzle)

matrix.printPuzzle()

print('\n')

print('Goal State:')
display(goal)
print('Initial State:')
display(initial)
print('the coordinate of Initial Zero is:', matrix.zero, '\n')

print(" ————————————")
print("【        START        】")
print(" ————————————")

print(matrix.puzzle)

m = 0
level = 0
visited_nodes = {}
visited_nodes[m] = initial


lists=copy.deepcopy(matrix)
while(1):


    if lists.puzzle == goal:
        print("the initial state equals to goal state. Please re-generate the initial state.")
        break
    getlist=copy.deepcopy(lists)
    left(lists, level, visited_nodes)

    lists=copy.deepcopy(getlist)
    right(lists, level, visited_nodes)

    lists=copy.deepcopy(getlist)
    up(lists, level, visited_nodes)

    lists=copy.deepcopy(getlist)
    down(lists, level, visited_nodes)

    print("The depth needs to increase for finding a solution")
    break

