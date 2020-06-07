# -*- coding: utf-8 -*-
"""used to write the global environment
"""
import process_program.global_env.global_demo as gl

gl._init()

gl.set_value('TIME_FILE_PATH', 'G:\\python\\nuclear_data_process_basic_template \
                                \\nuclear_data_analysis_program\\nuclear_data_ana \
                                \\origin_data\\SF_test\\faster_setup\\')
gl.set_value('EVENT_FILE_PATH', 'G:\\python\\nuclear_data_process_basic_template \
                                 \\nuclear_data_analysis_program\\nuclear_data_ana \
                                 \\origin_data\\SF_test\\event_data\\')
gl.set_value('BASIC_FILE_PATH', 'G:\\python\\nuclear_data_process_basic_template \
                                 \\nuclear_data_analysis_program\\nuclear_data_ana \
                                 \\origin_data\\')

gl.set_value('DB_FILE_1', 'G:\\python\\nuclear_data_process_basic_template \
                           \\nuclear_data_analysis_program\\nuclear_data_ana \
                           \\origin_data\\Origin_data.db')
gl.set_value('DB_FILE_2', 'G:\\python\\nuclear_data_process_basic_template \
                           \\nuclear_data_analysis_program\\nuclear_data_ana \
                           \\process_program\\Process_program.db')
gl.set_value('DB_FILE_3', 'G:\\python\\nuclear_data_process_basic_template \
                           \\nuclear_data_analysis_program\\nuclear_data_ana \
                           \\final_result\\final_result.db')
gl.set_value('DB_FILE_PATH_1', 'G:\\python\\nuclear_data_process_basic_template \
                                \\nuclear_data_analysis_program\\nuclear_data_ana \
                                \\origin_data\\')
gl.set_value('DB_FILE_PATH_2', 'G:\\python\\nuclear_data_process_basic_template \
                                \\nuclear_data_analysis_program\\nuclear_data_ana \
                                \\process_program\\')
gl.set_value('DB_FILE_PATH_3', 'G:\\python\\nuclear_data_process_basic_template \
                                \\nuclear_data_analysis_program\\nuclear_data_ana \
                                \\final_result\\')
gl.set_value('TABLE_NAME_01', 'exp_time_data')
gl.set_value('TABLE_NAME_02', 'exp_det_data')
gl.set_value('TABLE_NAME_03', 'exp_basic_data')
gl.set_value('TABLE_NAME_04', 'origin_data')
gl.set_value('TABLE_NAME_11', 'background_data')
gl.set_value('TABLE_NAME_12', 'experiment_data')
gl.set_value('TABLE_NAME_13', 'sf1_off_sf2_off_data')
gl.set_value('TABLE_NAME_14', 'sf1_on_sf2_off_data')
gl.set_value('TABLE_NAME_15', 'sf1_off_sf2_on_data')
gl.set_value('TABLE_NAME_16', 'sf1_on_sf2_on_data')
gl.set_value('TABLE_NAME_21', 'sf1_on_sf2_off_gc_v0_data')
gl.set_value('TABLE_NAME_22', 'sf1_off_sf2_on_gc_v4_pos_20_data')
gl.set_value('TABLE_NAME_23', 'A_P_test_result')
gl.set_value('SHOW_SQL', 'True')
