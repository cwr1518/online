
class Graph():

    def __init__(self,filename):
        self.left=[]
        self.right=[]
        self.edge=[]
        self.filename=filename
        self.line=0

    def input_new_point(self,round):
        with open(self.filename,encoding='utf-8') as file_object:
            lines=file_object.readlines()
        start_tag='第'+str(round)+'轮'+'\n'
        if lines[self.line]==start_tag:
            #print("jinru")
            self.line=self.line+2
            if lines[self.line]!="右边\n":
                l_=list(map(int,lines[self.line].split(' ')))
                l_.append(0)
                self.left.append(l_)
                self.line=self.line+2
                if lines[self.line]!="边值\n":  #该操建立在每次双边都会来的基础上
                    r_=list(map(int,lines[self.line].split(' ')))
                    r_.append(0)
                    self.right.append(r_)
                    self.line=self.line+2
                else:
                    self.line=self.line+1
            else:
                self.line=self.line+1
                if lines[self.line]!="边值\n":  #左边无点到来，右边有
                    r_ = list(map(int, lines[self.line].split(' ')))
                    r_.append(0)
                    self.right.append(r_)
                    self.line=self.line+2
                else:
                    self.line=self.line+1
            while lines[self.line]!="第"+str(round+1)+"轮"+"\n" and self.line!=len(lines):
                edge_temp=list(map(float,lines[self.line].split(' ')))
                #print(len(self.left),"h")
                for i in range(len(self.left)):
                    if edge_temp[0]==self.left[i][0]:
                        for ii in range(len(self.right)):
                            if edge_temp[1]==self.right[ii][0]:
                                self.edge.append(edge_temp)
                self.line=self.line+1
                if self.line==len(lines):
                    break

    def delet_edge(self,list, l_num, r_num):
        dele_edge = []
        for ii in range(len(list)):
            if list[ii][0] == l_num:
                dele_edge.append(ii)
            # print("应删除",list[ii][0])
            elif list[ii][1] == r_num:
                dele_edge.append(ii)
        for ii in range(len(dele_edge)):
            #  print("实际删除",list[dele_edge[len(dele_edge)-ii-1]][0])
            list.pop(dele_edge[len(dele_edge) - ii - 1])

    def time_update(self):
        l_timeout = []
        r_timeout = []
        for lk in range(len(self.left)):  # 这一行开始到21行是在实时刷新每个点剩余生存时间，同时剩余生存时间为0的点被去除
            if (self.left[lk][1] == 0):
                l_timeout.append(lk)
            self.left[lk][1] = self.left[lk][1] - 1
        for rk in range(len(self.right)):
            if (self.right[rk][1] == 0):
                r_timeout.append(rk)
            self.right[rk][1] = self.right[rk][1] - 1
        for tout in range(len(l_timeout)):
            self.delet_edge(self.edge, self.left[l_timeout[len(l_timeout) - tout - 1]][0], ' ')
            self.left.pop(l_timeout[len(l_timeout) - tout - 1])
        for tout in range(len(r_timeout)):
            self.delet_edge(self.edge, ' ', self.right[r_timeout[len(r_timeout) - tout - 1]][0])
            self.right.pop(r_timeout[len(r_timeout) - tout - 1])
        if self.left:
            for lk in range(len(self.left)):
                self.left[lk][2]=self.left[lk][2]+1
        if self.right:
            for rk in range(len(self.right)):
                self.right[rk][2]=self.right[rk][2]+1
    def existing_time(self):
        l=0
        r=0
        if self.left:
            for lk in range(len(self.left)):
                l=self.left[lk][2]+l
        if self.right:
            for rk in range(len(self.right)):
                r=self.right[rk][2]+r
        mean=(l+r)/(len(self.left)+len(self.right))
        return mean