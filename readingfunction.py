from graph import Graph
from print_state import print_state
from match import matching
import time_update
import match

filename="1.txt"
graph=Graph(filename)
u=0
for i in range(20):
    graph.time_update()
    graph.input_new_point(i)
    u=matching(graph.left,graph.right,graph.edge)+u
    print_state(graph.left,graph.right,graph.edge,i)
    print("得分",u)

