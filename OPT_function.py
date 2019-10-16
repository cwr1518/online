from graph import Graph
from print_state import print_state
from match import matching
import time_update
import match
import os
import time


filename="16_15_1.5.txt"
module_path = os.path.dirname(__file__)
time_number=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
logfile=str(module_path+"/optlog/"+filename+"log"+filename)
file_handle=open(logfile,mode="w")

graph=Graph(filename)
u=0
i=0
record=0
while True:
    graph.input_new_point(i)
    if i!=0 and i%1000==0:
        record=matching(graph.left,graph.right,graph.edge)
        u=u+record
        print("得分",u,"轮数",i)
        file_handle.write("得分"+str(u)+" "+"轮数"+str(i)+"\n")
        file_handle.write("比上四千轮增加："+str(record)+"\n")
    #if i%10==0:

    #print_state(graph.left,graph.right,graph.edge,i)


    i=i+1
