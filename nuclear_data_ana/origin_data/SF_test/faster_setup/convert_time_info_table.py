import os
from datetime import datetime
import numpy as np
 
def eachFile(filepath):
    global N_files
    N_files=0
    pathDir = os.listdir(filepath)   #获取当前路径下的文件名，返回list
    for s in pathDir:
        newDir=os.path.join(filepath,s)   #将文件名写入到当前文件路径后面
        if os.path.splitext(newDir)[1]==".setup":  #判断是否是txt
            list_total.append(s.split('.')[0])   #list0
            readFile(newDir)
            N_files=N_files+1
            pass

def readFile(filepath):
    index=0                  #控制数据存入不同的list
    with open(filepath,"r") as f:
        line_temp=f.readline()
        line=f.readline() #as the first line is blank, so I need to read twice
        while line:
            if line[:18]=='- Event count  : 0':     #根据关键词抽取数据
                index11,index12,index13,index14,data1,time1=f.readline().split()
                start=data1+' '+time1
                start=datetime.strptime(start,'%d-%m-%Y %H:%M:%S')
                list_total.append(str(start))   # start time
                index21,index22,index23,index24,data2,time2=f.readline().split()
                stop=data2+' '+time2
                stop=datetime.strptime(stop,'%d-%m-%Y %H:%M:%S')
                list_total.append(str(stop))   # stop time
#                time_dif='{:.2f}'.format((stop-start).total_seconds()) #time unit second
                time_dif=(stop-start).total_seconds() #time unit second
                list_total.append(str(time_dif))   # time difference unit TypeError: write() argument must be str, not datetime.datetime
            line=f.readline()


def main():
    global list_total      #定义全局变量，可以将所有数据都存入list中
    fp=r'G:\\SF_test\\faster_setup' #存放数据的目录
    os.chdir(fp)
    eachFile(fp)
    output =open("sp_tset_time_info.dat",'w')    #将list存入相应的文件中，便于后期处理数据
    listdata_total=list(np.reshape(list_total,(N_files,4)))    #改变数组维度，存储
    output.write('name start_time stop_time duration\n')
    for i in range(N_files):                      #数据读入相应文件的第一种方法，第一篇博客有介绍
        for j in range(4):
            output.write(listdata_total[i][j]+' ')
#            output.write('\t')
        output.write('\n')
    output.close()
 
if __name__ == '__main__':
    list_total=[]
    main()