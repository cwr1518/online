import random

def create_left_node(left,right,edge,l_num):
    ltemp=[l_num,random.randint(9,18)]  #设置生存时间
    left.append(ltemp)
    for rk in range(len(right)):
        if(random.randint(2,6)>3):
            edge_temp=[l_num,right[rk][0],random.randint(1,5)]
            edge.append(edge_temp)

def create_right_node(left,right,edge,r_num):
    rtemp=[r_num,random.randint(9,18)]  #设置生存时间
    right.append(rtemp)
    for lk in range(len(left)):
        if(random.randint(2,6)>3):
            edge_temp=[left[lk][0],r_num,random.randint(1,5)]
            edge.append(edge_temp)
