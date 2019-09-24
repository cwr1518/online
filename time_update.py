from edge_action import delet_edge

def time_update(left,right,edge):
    l_timeout=[]
    r_timeout=[]
    for lk in range(len(left)):        #这一行开始到21行是在实时刷新每个点剩余生存时间，同时剩余生存时间为0的点被去除
        if(left[lk][1]==0):
            l_timeout.append(lk)
        left[lk][1]=left[lk][1]-1
    for rk in range(len(right)):
        if(right[rk][1]==0):
            r_timeout.append(rk)
        right[rk][1]=right[rk][1]-1
    for tout in range(len(l_timeout)):
        delet_edge(edge,left[l_timeout[len(l_timeout)-tout-1]][0],' ')
        left.pop(l_timeout[len(l_timeout)-tout-1])
    for tout in range(len(r_timeout)):
        delet_edge(edge,' ',right[r_timeout[len(r_timeout)-tout-1]][0])
        right.pop(r_timeout[len(r_timeout)-tout-1])
