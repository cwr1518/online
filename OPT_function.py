from graph import Graph
from print_state import print_state
from match import matching
import time_update
import match

filename="11.txt"
file_handle=open("optlog.txt",mode="w")
graph=Graph(filename)
u=0
i=0
while True:
    graph.input_new_point(i)
    if i and i%1000==0:
        u=matching(graph.left,graph.right,graph.edge)+u
        print("得分",u,"轮数",i)
        file_handle.write("得分"+str(u)+" "+"轮数"+str(i)+"\n")
    #if i%10==0:

    #print_state(graph.left,graph.right,graph.edge,i)


    i=i+1
