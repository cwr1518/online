from graph import Graph
import numpy as np
from match import matching
import time_update
import math
import time
import os

X=np.full(15,80)+np.random.rand(15)
N=np.zeros(15)
arms=X
gama=0.95
epsilon=0.08
module_path = os.path.dirname(__file__)
filename="D-4000-2.txt"
#time_number=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
#logfile=str(module_path+"/greedylog/"+"greedylog"+filename)

#file_handle=open(logfile,mode="w")
graph=Graph(filename)
u=0
i=0
B=100
all_reward=0
record=0
record_old=0
batch=arms.argmax()
N[batch]=2
while True:
    if i!=0 and i%80==0:
        u=matching(graph.left,graph.right,graph.edge)
        record=u+record
        all_reward=u+all_reward
        X=X*gama
        N=N*gama
        X[batch]=X[batch]+record
        N[batch]=N[batch]+1
        n=np.sum(N)
        c=2*B*((epsilon*math.log10(n)/N)**0.5)
        arms=X/N+c
        arms[0],arms[1],arms[2],arms[4], arms[6],arms[8],arms[10],arms[12],arms[14]=0,0,0,0,0,0,0,0,0
        batch=np.argmax(arms)
        print("轮数",i,"batch",batch,"得分",record,"\n",N,"总分",all_reward,"\n",X,"\n")
        record=0

    graph.time_update()
    graph.input_new_point(i)
    l=graph.existing_time()

    if i%batch==0:
        u=matching(graph.left,graph.right,graph.edge)
        record=u+record
        all_reward=u+all_reward
    #print_state(graph.left,graph.right,graph.edge,i)
    #if i%1000==0:
     #       record=all_reward
      #      file_handle.write("得分"+str(all_reward)+" "+"轮数"+str(i)+"\n")
       #     file_handle.write("比上一千轮增加："+str(record-record_old)+"\n")
        #    file_handle.write("\n")
         #   record_old=record
    #print("得分",all_reward,"轮数",i,"batch为",batch)
    i=i+1



