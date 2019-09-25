
class Graph():

    def __init__(self,filename,line,round):
        self.left
        self.right
        self.edge
        self.filename=filename
        self.line=line
        self.round=round

    def input_new_point(self,filename):
        with open(self.filename) as file_object:
            lines=file_object.readline()
        start_tag="第"+str(self.round)+"轮"
        if lines[self.line]==start_tag:
            self.line=self.line+2
            if lines[self.line]!="右边":
                self.left.append(list(map(int,lines[self.line].split(' '))))
                self.line=self.line+2
                if lines[self.line]!="边值":  #该操建立在每次双边都会来的基础上
                    self.right.append(list(map(int,lines[self.line].split(' '))))
                    self.line=self.line+2
                else:
                    self.line=self.line+1
            else:
                self.line=self.line+1
                if lines[self.line]!="边值":  #左边无点到来，右边有
                    self.right.append(list(map(int,lines[self.line].split(' '))))
                    self.line=self.line+2
                else:
                    self.line=self.line+1
            while lines[self.line]!="第"+str(self.round+1)+"轮":
                edge_temp=list(map(int,lines[self.line].split(' ')))
                for i in range(len(self.left)):
                    if edge_temp[0]==self.left[0]:
                        for ii in range(len(self.right)):
                            if edge_temp[1]==self.right[0]:
                                self.edge.append(edge_temp)
                self.line=self.line+1


