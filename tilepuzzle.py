import puzzle 
import sys

t=puzzle.TilePuzzle(int(sys.argv[1]))
t.permute(int(sys.argv[2]))
t.printPuzzle()

