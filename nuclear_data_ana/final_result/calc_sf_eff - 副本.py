# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 17:47:51 2019

@author: chenjianqi
"""
import matplotlib.pyplot as plt
from process_program.process_program import *
from process_program.global_env.read import A
import numpy as np
import math
import sqlite3

class calc_sf_eff:
    
    def __init__(self,table12,table23):
        self.table12=table12
        self.table23=table23

    def calc_sf_eff(self,conn,table12,table23):

        c=get_cursor(conn)
        c.execute('''ATTACH [{}] as BM '''.format(A.DB_FILE_2))
        # start from file NY_SF1_OFF_15kHz_SF2_OFF_13kHz_25cm_withoutGCv4_bis
        c.execute("insert into [{}] select * from BM.[{}] limit 24 offset 90".format(table23,table12))
        y = c.execute("select * from [{}]".format(table23)).fetchall()
        conn.commit()
        c.execute("DETACH DATABASE 'BM'")

        sf2_frequency = []
        N_ucn_gadget_time_offset_0 = []
        N_ucn_gadget_time_offset_10 = []
        N_ucn_gadget_time_offset_20 = []
        N_ucn_Nanosc_1_time_offset_0 = []
        N_ucn_Nanosc_2_time_offset_0 = []
        N_ucn_Nanosc_1_time_offset_10 = []
        N_ucn_Nanosc_2_time_offset_10 = []
        N_ucn_Nanosc_1_time_offset_20 = []
        N_ucn_Nanosc_2_time_offset_20 = []
        N_ucn_norm_time_offset_0 = []
        N_ucn_norm_time_offset_10 = []
        N_ucn_norm_time_offset_20 = []
        Ucertainty_N_ucn_norm_time_offset_0 = []
        Ucertainty_N_ucn_norm_time_offset_10 = []
        Ucertainty_N_ucn_norm_time_offset_20 = []
        Ucertainty_listdata_total_0 = []
        Ucertainty_listdata_total_10 = []
        Ucertainty_listdata_total_20 = []
        Duration = []
#      calculate variable
        for i in range(len(y)):
            print(y[i][1],' ',y[i][15],' ',y[i][16],' ',y[i][17])
            sf2_frequency.append(y[i][12]) # f2 frequency
            N_ucn_gadget_time_offset_0.append(y[i][15])
            N_ucn_gadget_time_offset_10.append(y[i][16])
            N_ucn_gadget_time_offset_20.append(y[i][17])
            N_ucn_Nanosc_1_time_offset_0.append(y[i][18])
            N_ucn_Nanosc_2_time_offset_0.append(y[i][19])
            N_ucn_Nanosc_1_time_offset_10.append(y[i][20])
            N_ucn_Nanosc_2_time_offset_10.append(y[i][21])
            N_ucn_Nanosc_1_time_offset_20.append(y[i][22])
            N_ucn_Nanosc_2_time_offset_20.append(y[i][23])
            Duration.append(y[i][26])

            # N_ucn_norm_time_offset_temp_0 = N_ucn_gadget_time_offset_0[i]*(N_ucn_Nanosc_1_time_offset_0[0]+N_ucn_Nanosc_2_time_offset_0[0])/(N_ucn_Nanosc_1_time_offset_0[i]+N_ucn_Nanosc_2_time_offset_0[i])
            # N_ucn_norm_time_offset_temp_0 = N_ucn_norm_time_offset_temp_0*Duration[0]/Duration[i]
            # N_ucn_norm_time_offset_0.append(N_ucn_norm_time_offset_temp_0)
            # Ucertainty_N_ucn_norm_time_offset_0.append(math.sqrt(N_ucn_norm_time_offset_temp_0))

            N_ucn_norm_time_offset_temp_0 = N_ucn_gadget_time_offset_0[i]/(N_ucn_Nanosc_1_time_offset_0[i]+N_ucn_Nanosc_2_time_offset_0[i])
           # N_ucn_norm_time_offset_temp_0 = N_ucn_norm_time_offset_temp_0*Duration[0]/Duration[i]
            N_ucn_norm_time_offset_0.append(N_ucn_norm_time_offset_temp_0)
            Ucertainty_N_ucn_norm_time_offset_0.append(math.sqrt(N_ucn_norm_time_offset_temp_0))

            N_ucn_norm_time_offset_temp_10 = N_ucn_gadget_time_offset_10[i]/(N_ucn_Nanosc_1_time_offset_10[i]+N_ucn_Nanosc_2_time_offset_10[i])
           # N_ucn_norm_time_offset_temp_0 = N_ucn_norm_time_offset_temp_0*Duration[0]/Duration[i]
            N_ucn_norm_time_offset_10.append(N_ucn_norm_time_offset_temp_10)
            Ucertainty_N_ucn_norm_time_offset_10.append(math.sqrt(N_ucn_norm_time_offset_temp_10))

            N_ucn_norm_time_offset_temp_20 = N_ucn_gadget_time_offset_20[i]/(N_ucn_Nanosc_1_time_offset_20[i]+N_ucn_Nanosc_2_time_offset_20[i])
           # N_ucn_norm_time_offset_temp_0 = N_ucn_norm_time_offset_temp_0*Duration[0]/Duration[i]
            N_ucn_norm_time_offset_20.append(N_ucn_norm_time_offset_temp_20)
            Ucertainty_N_ucn_norm_time_offset_20.append(math.sqrt(N_ucn_norm_time_offset_temp_20))


        listdata_total_0=list(np.reshape(N_ucn_norm_time_offset_0,(6,4)))
        listdata_total_10=list(np.reshape(N_ucn_norm_time_offset_10,(6,4)))
        listdata_total_20=list(np.reshape(N_ucn_norm_time_offset_20,(6,4)))
        print(listdata_total_0,'\n\n',listdata_total_10,'\n\n',listdata_total_20,'\n\n')



        Ucertainty_listdata_total_0=list(np.reshape(Ucertainty_N_ucn_norm_time_offset_0,(6,4)))
        Ucertainty_listdata_total_10=list(np.reshape(Ucertainty_N_ucn_norm_time_offset_10,(6,4)))
        Ucertainty_listdata_total_20=list(np.reshape(Ucertainty_N_ucn_norm_time_offset_20,(6,4)))



        f_offset_0=np.empty((len(listdata_total_0),4),dtype=float)
        f_offset_10=np.empty((len(listdata_total_10),4),dtype=float)
        f_offset_20=np.empty((len(listdata_total_20),4),dtype=float)
        
        for i in range(1,len(listdata_total_0)+1):
        #victor version

             f_offset_0[i-1][0] = (listdata_total_0[i-1][3]-listdata_total_0[i-1][1])*100/(listdata_total_0[i-1][0]-listdata_total_0[i-1][2])
             f_offset_0[i-1][1] = f_offset_0[i-1][2]*math.sqrt((Ucertainty_listdata_total_0[i-1][0]/(listdata_total_0[i-1][0]-listdata_total_0[i-1][2]))**2\
                                                              +(Ucertainty_listdata_total_0[i-1][2]/(listdata_total_0[i-1][0]-listdata_total_0[i-1][2]))**2\
                                                              +(Ucertainty_listdata_total_0[i-1][3]/(listdata_total_0[i-1][3]-listdata_total_0[i-1][1]))**2\
                                                              +(Ucertainty_listdata_total_0[i-1][1]/(listdata_total_0[i-1][3]-listdata_total_0[i-1][1]))**2)

             f_offset_0[i-1][2] = (listdata_total_0[i-1][3]-listdata_total_0[i-1][2])*100/(listdata_total_0[i-1][0]-listdata_total_0[i-1][1])
             f_offset_0[i-1][3] = f_offset_0[i-1][0]*math.sqrt((Ucertainty_listdata_total_0[i-1][0]/(listdata_total_0[i-1][0]-listdata_total_0[i-1][1]))**2\
                                                              +(Ucertainty_listdata_total_0[i-1][1]/(listdata_total_0[i-1][0]-listdata_total_0[i-1][1]))**2\
                                                              +(Ucertainty_listdata_total_0[i-1][2]/(listdata_total_0[i-1][3]-listdata_total_0[i-1][2]))**2\
                                                              +(Ucertainty_listdata_total_0[i-1][3]/(listdata_total_0[i-1][3]-listdata_total_0[i-1][2]))**2)
        print(f_offset_0,'\n\n',f_offset_10,'\n\n',f_offset_20) 

        
Obj_calc_sf_eff = calc_sf_eff(A.TABLE_NAME_12,A.TABLE_NAME_23) 