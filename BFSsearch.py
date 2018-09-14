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
    if lists.puzzle in visited_nodes.values():
        return 1
    else:
        return 0

start=time.time()

i = 0
q = queue.Queue()  # define queue data structure
visited = 0

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

level = 0
visited_nodes = {}
visited_nodes[i] = initial
q.put(matrix)
q.put(level)
q.put('x')


while(q.empty()==0):
    getlist=copy.deepcopy(q.get())
    lists=copy.deepcopy(getlist)
    level=q.get()
    level=level+1
    prev_pos=q.get()

    if lists.puzzle == goal:
        print("the initial state equals to goal state. Please re-generate the initial state.")
        break

    l = check_validity_operate(lists, "left", prev_pos )
    if l == 1:
        print( "LEVEL ", level,"\n" )
        lists.printPuzzle()
        lists.doMove("L")
        print("Moving L")
        lists.printPuzzle()
        print("\n")
        if check_visited(lists,visited_nodes) == 0:
            if lists.checkPuzzle()!=True:
                q.put(copy.deepcopy(lists))
                q.put(level)
                q.put('l')
                i = i + 1
                visited_nodes[i] = copy.deepcopy(lists.puzzle)
            else:
                i = i + 1
                print ("Final state reached")
                print( "Total no of nodes generated ", i)
                break


    lists = copy.deepcopy(getlist)
    r = check_validity_operate(lists, "right", prev_pos )
    if r == 1:
        print( "LEVEL ", level,"\n")
        lists.printPuzzle()
        lists.doMove("R")
        print("Moving R")
        lists.printPuzzle()
        print("\n")
        if check_visited(lists, visited_nodes) == 0:
            if lists.checkPuzzle()!=True:
                q.put(copy.deepcopy(lists))
                q.put(level)
                q.put('r')
                i = i + 1
                visited_nodes[i] = copy.deepcopy(lists.puzzle)
            else:
                i = i + 1
                print ("Final state reached")
                print( "Total no of nodes generated ", i)
                print ("Visited nodes found ", visited)
                break


    lists = copy.deepcopy(getlist)
    u = check_validity_operate(lists, "up", prev_pos )
    if u == 1:
        print( "LEVEL ", level,"\n" )
        lists.printPuzzle()
        lists.doMove("U")
        print("Moving U")
        lists.printPuzzle()
        print("\n")
        if check_visited(lists, visited_nodes) == 0:
            if lists.checkPuzzle()!=True:
                q.put(copy.deepcopy(lists))
                q.put(level)
                q.put('u')
                i = i + 1
                visited_nodes[i] = copy.deepcopy(lists.puzzle)
            else:
                i = i + 1
                print ("Final state reached")
                print( "Total no of nodes generated ", i)
                print ("Visited nodes found ", visited)
                break

    lists = copy.deepcopy(getlist)
    d = check_validity_operate(lists, "down", prev_pos )
    if d == 1:
        print( "LEVEL ", level,"\n" )
        lists.printPuzzle()
        lists.doMove("D")
        print("Moving D")
        lists.printPuzzle()
        print("\n")
        if check_visited(lists, visited_nodes) == 0:
            if lists.checkPuzzle()!=True:
                q.put(copy.deepcopy(lists))
                q.put(level)
                q.put('d')
                i = i + 1
                visited_nodes[i] = copy.deepcopy(lists.puzzle)
            else:
                i = i + 1
                print ("Final state reached")
                print ("Total no of nodes generated ", i)
                print ("Visited nodes found ", visited)
                break
end=time.time()
print("Time consumption:", end-start)




