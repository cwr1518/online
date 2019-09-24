
def delet_edge(list,l_num,r_num):
    dele_edge=[]
    for ii in range(len(list)):
        if list[ii][0]==l_num :
            dele_edge.append(ii)
           # print("应删除",list[ii][0])
        elif list[ii][1]==r_num:
            dele_edge.append(ii)
    for ii in range(len(dele_edge)):
      #  print("实际删除",list[dele_edge[len(dele_edge)-ii-1]][0])
        list.pop(dele_edge[len(dele_edge)-ii-1])
