
#-*- coding : utf-8 -*-
# coding: utf-8

from graph import Graph
from print_state import print_state
from match import matching
import time_update
import match

filename="11.txt"
file_handle=open("readinglog.txt",mode="w")
graph=Graph(filename)
u=0
i=0
while True:
    graph.time_update()
    graph.input_new_point(i)
    #if i%10==0:
    u=matching(graph.left,graph.right,graph.edge)+u
    #print_state(graph.left,graph.right,graph.edge,i)
    file_handle.write("得分"+str(u)+" "+"轮数"+str(i)+"\n")
    print("得分",u,"轮数",i)
    i=i+1

