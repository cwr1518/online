#-*- coding : utf-8 -*-
# coding: utf-8
from graph import Graph
from print_state import print_state
from match import matching
import time_update
import match
import time
import os

module_path = os.path.dirname(__file__)
filename="D-4000-2.txt"
time_number=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
logfile=str(module_path+"/greedylog/"+"greedylog"+filename)

file_handle=open(logfile,mode="w")
graph=Graph(filename)
u=0
i=0
all_reward=0
record=0
record_old=0
while True:

    graph.time_update()
    graph.input_new_point(i)
    l=graph.existing_time()

    if i%15==0:
        u=matching(graph.left,graph.right,graph.edge)
        all_reward=u+all_reward
    #print_state(graph.left,graph.right,graph.edge,i)
    if i%1000==0:
            record=all_reward
            file_handle.write("得分"+str(all_reward)+" "+"轮数"+str(i)+"\n")
            file_handle.write("比上一千轮增加："+str(record-record_old)+"\n")
            file_handle.write("\n")
            record_old=record
    print("得分",all_reward,"轮数",i)
    i=i+1

