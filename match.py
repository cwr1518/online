from scipy.optimize import linear_sum_assignment
import numpy as np
from edge_action import delet_edge

def matching(left,right,edge):
    if left and right and edge:
        M_size=max(len(left),len(right))
        matrix=[]
        right_dic={}
        for i in range(M_size):
            if i<len(right):
                right_dic[right[i][0]]=i
        for i in range(M_size):
            if i<len(left):
                row=[0]*M_size
                for j in range(len(edge)):
                    if left[i][0]==edge[j][0]:
                        row[right_dic[edge[j][1]]]=edge[j][2]
                matrix.append(row)
            else:
                row=[0]*M_size
                matrix.append(row)
            print(row)
        matrix=matrix
        cost=np.array(matrix)
        cost=100-cost
        row_ind,col_ind=linear_sum_assignment(cost)
        print(row_ind)
        print(col_ind)
        cost=100-cost
        u1=cost[row_ind,col_ind].sum()
        right_delet=[]
        left_delet=[]
        for i in range(M_size):
            if matrix[i][col_ind[i]]>0:
                left_delet.append(i)
                right_delet.append(col_ind[i])
        right_delet.sort()
        for i in range(len(left_delet)):
            delet_edge(edge,left[left_delet[len(left_delet)-i-1]][0],' ')
            left.pop(left_delet[len(left_delet)-i-1])
        for i in range(len(right_delet)):
            delet_edge(edge,' ',right[right_delet[len(right_delet)-i-1]][0])
            right.pop(right_delet[len(right_delet)-i-1])
        return u1
    else:
        return 0
