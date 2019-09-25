import random
from edge_action import delet_edge
from time_update import time_update
from create_node import create_left_node
from create_node import create_right_node
from match import matching
import print_state
left=[]
right=[]
edge=[]
l_num=0
r_num=0
u=0
file_handle=open("1.txt",mode="w")
for i in range(20):
    edge_temp=[]
    time_update(left,right,edge)
    file_handle.writelines(["第",str(i),"轮\n"])
    file_handle.write("左边\n")
    if(random.randint(1,4)>2):   #决定了左边点到来的频率，以及生存时间
        l_num=l_num+1
        create_left_node(left,right,edge,l_num,edge_temp,file_handle)
    file_handle.write("右边\n")
    if(random.randint(1,4)>2):   #决定了右边点到来的频率，以及生存时间
        r_num=r_num+1
        create_right_node(left,right,edge,r_num,edge_temp,file_handle)
    file_handle.write("边值\n")
    for ii in range(len(edge_temp)):
        file_handle.writelines([str(edge_temp[ii][0])," ",str(edge_temp[ii][1])," ",str(edge_temp[ii][2]),"\n"])
    print_state.print_state(left,right,edge,i)
    #print("matric:")
    #if i%9==0:
     #   u=matching(left,right,edge)+u
    #print("uility:",u)

