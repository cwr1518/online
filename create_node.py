import random
#file_handle=open("1.txt",mode="w")
def create_left_node(left,right,edge,l_num,edge_temp1,file_handle):
    ltemp=[l_num,random.randint(30,50)]  #设置生存时间
    left.append(ltemp)
    file_handle.writelines([str(ltemp[0])," ",str(ltemp[1]),"\n"])
    for rk in range(len(right)):
        if(random.randint(2,6)>=3):
            edge_temp=[l_num,right[rk][0],random.normalvariate(0.5,0.3)]
            edge.append(edge_temp)
            edge_temp1.append(edge_temp)

def create_right_node(left,right,edge,r_num,edge_temp1,file_handle):
    rtemp=[r_num,random.randint(30,50)]  #设置生存时间
    right.append(rtemp)
    file_handle.writelines([str(rtemp[0])," ",str(rtemp[1]),"\n"])
    for lk in range(len(left)):
        if(random.randint(2,6)>=3):
            edge_temp=[left[lk][0],r_num,random.normalvariate(0.5,0.3)]
            edge.append(edge_temp)
            edge_temp1.append(edge_temp)
