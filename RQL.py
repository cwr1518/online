from graph import Graph
import random
from print_state import print_state
from match import matching
import time_update

filename="1.txt"
graph=Graph(filename)
u=0
alpha=1
lmin=8
lmax=16
C=16
H=19999
u=0
#初始化Q表
Q={}
for i in range(C):
    for ii in range(C):
        for iii in range(lmin,lmax):
            for iiii in range(iii,lmax):
                Q_temp=(i,ii,iii,iiii)
                Q[Q_temp]=random.randint(9,15)

#执行
for i in range(1):
    for t in range(lmin):
        graph.time_update()
        graph.input_new_point(t)
    print(t,"l")
    l_num=len(graph.left)
    r_num=len(graph.right)
    t=lmin
    l=lmin
    while t<H:
        q=0
        l_temp=0
        #找到最大的Q值对应的ll
        for ll in range(l,lmax):
            if Q[(l_num,r_num,l,ll)]>q:
                q=Q[(l_num,r_num,l,ll)]
                l_temp=ll
        if l_temp==l:
            r=matching(graph.left,graph.right,graph.edge)
            u=u+r
            tt=0
            for tt in range(lmin):
                graph.time_update()
                graph.input_new_point(t+tt)
            #l_numl是为了与原来的l_num做区分，即st+lmin。。。
            l_numl=len(graph.left)
            r_numl=len(graph.right)
            #求maxl Q((st+lmin , lmin), l)
            l_temp1=0
            q1=0
            ll=0
            for ll in range(lmin,lmax):
                if Q[(l_numl,r_numl,lmin,ll)]>q1:
                    q1=Q[(l_numl,r_numl,lmin,ll)]
                    l_temp1=ll
            Q[(l_num,r_num,l,l_temp)]=Q[(l_num,r_num,l,l_temp)]+alpha*(r+q1-Q[(l_num,r_num,l,l_temp)])
            t=t+lmin
            l=lmin
        else:
            graph.time_update()
            graph.input_new_point(t)
            l_numl=len(graph.left)
            r_numl=len(graph.right)
            q1=0
            ll=0
            for ll in range(l+1,lmax):
                if Q[(l_numl,r_numl,l+1,ll)]>q1:
                    q1=Q[(l_numl,r_numl,l+1,ll)]
                    l_temp1=ll
            Q[(l_num,r_num,l,l_temp)]=Q[(l_num,r_num,l,l_temp)]+alpha*(q1-Q[(l_num,r_num,l,l_temp)])
            l=l+1
            t=t+1
        #print_state(graph.left,graph.right,graph.edge,i)
        print("得分",u,"轮数",t)
