file_handle=open("2.txt",mode="w")
def print_state(left,right,edge,i):
    print("第",i,"轮")
    file_handle.writelines(["第",str(i),"轮\n"])
    print(("左边"))
    file_handle.write("左边\n")
    for ii in range(len(left)):
        print(left[ii][0])
        file_handle.writelines([str(left[ii][0]),"\n"])
    print("右边")
    file_handle.write("右边\n")
    for ii in range(len(right)):
        print(right[ii][0])
        file_handle.writelines([str(right[ii][0]),"\n"])
    print("边值")
    file_handle.write("边值\n")
    for ii in range(len(edge)):
        print(edge[ii][0]," ",edge[ii][1]," ",edge[ii][2])
        file_handle.writelines([str(edge[ii][0])," ",str(edge[ii][1])," ",str(edge[ii][2]),"\n"])
