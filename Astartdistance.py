import puzzle
import sys
import queue
import copy
import time
from heapq import *


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
def getpos(lists,value):
    for x in range(0 ,3):
        for y in range(0 ,3):
            if lists.puzzle[x][y]==value:
                return (x,y)

def getdis(lists):
    a0=getpos(lists,0)
    a1=getpos(lists,1)
    a2=getpos(lists,2)
    a3=getpos(lists,3)
    a4=getpos(lists,4)
    a5=getpos(lists,5)
    a6=getpos(lists,6)
    a7=getpos(lists,7)
    a8=getpos(lists,8)

    dis0=abs(a0[0]-2)+abs(a0[1]-2)
    dis1=abs(a1[0]-0)+abs(a1[1]-0)
    dis2=abs(a2[0]-0)+abs(a2[1]-1)
    dis3=abs(a3[0]-0)+abs(a3[1]-2)
    dis4=abs(a4[0]-1)+abs(a4[1]-0)
    dis5=abs(a5[0]-1)+abs(a5[1]-1)
    dis6=abs(a6[0]-1)+abs(a6[1]-2)
    dis7=abs(a7[0]-2)+abs(a7[1]-0)
    dis8=abs(a8[0]-2)+abs(a8[1]-1)

    dis=dis0+dis1+dis2+dis3+dis4+dis5+dis6+dis7+dis8
    return dis

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

heap=[]
item=[getdis(matrix), '0',level,'x']
heappush(heap,item)

while heap:
    get_item=heappop(heap)
    if get_item[1] == '1':
       getlist=copy.deepcopy(item1)
    elif get_item[1]=='2':
        getlist=copy.deepcopy(item2)
    elif get_item[1]=='3':
         getlist=copy.deepcopy(item3)
    elif get_item[1]=='4':
         getlist=copy.deepcopy(item4)
    else:
        getlist=copy.deepcopy(matrix)

    lists=copy.deepcopy(getlist)
    level=get_item[2]
    level=level+1
    prev_pos=get_item[3]

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
                item=[getdis(lists),'1',level,'l']
                item1=copy.deepcopy(lists)
                heappush(heap,item)
                i = i + 1
                visited_nodes[i] = copy.deepcopy(lists.puzzle)
                print('the accmulated distance is:',getdis(lists))
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
                item=[getdis(lists),'2',level,'r']
                item2=copy.deepcopy(lists)
                heappush(heap,item)
                i = i + 1
                visited_nodes[i] = copy.deepcopy(lists.puzzle)
                print('the accmulated distance is:',getdis(lists))
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
                item=[getdis(lists),'3', level,'u']
                heappush(heap,item)
                item3=copy.deepcopy(lists)
                i = i + 1
                visited_nodes[i] = copy.deepcopy(lists.puzzle)
                print('the accmulated distance is:',getdis(lists))
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
                item=[getdis(lists),'4', level,'d']
                item4=copy.deepcopy(lists)
                heappush(heap,item)
                i = i + 1
                visited_nodes[i] = copy.deepcopy(lists.puzzle)
                print('the accmulated distance is:',getdis(lists))
            else:
                i = i + 1
                print ("Final state reached")
                print ("Total no of nodes generated ", i)
                print ("Visited nodes found ", visited)
                break

end=time.time()
print("Time consumption:", end-start)
