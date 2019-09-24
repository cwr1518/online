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


for i in range(1000):
    time_update(left,right,edge)
    if(random.randint(1,4)>2):   #决定了左边点到来的频率，以及生存时间
        l_num=l_num+1
        create_left_node(left,right,edge,l_num)
    if(random.randint(1,4)>2):   #决定了右边点到来的频率，以及生存时间
        r_num=r_num+1
        create_right_node(left,right,edge,r_num)
    print_state.print_state(left,right,edge,i)
    #print("matric:")
    #if i%9==0:
     #   u=matching(left,right,edge)+u
    #print("uility:",u)

