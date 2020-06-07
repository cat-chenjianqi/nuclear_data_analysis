"""This module's docstring summary line.
   creat table_04
"""
from process_program.global_env.all_tables import create_table04_sql
from process_program.global_env.basic_fun import get_cursor, drop_table, create_table


def init_origin_data(conn, table01, table02, table03, table04):
    """initialize the origin table04 by table01, table02 and table03.
    """
    c = get_cursor(conn)
    drop_table(conn, table04)
    # create origin data
    create_table(conn, create_table04_sql)

    # update table04 with table03
    c.execute("Insert into[{}](id, run, name, beam, valve, guiding_coil_version, \
                               guiding_coil_condition, measured_times, \
                               sf1_position, sf2_position, sf1_frequency, \
                               sf1_current, sf1_amplitude, sf2_frequency, \
                               sf2_current, sf2_amplitude) \
              select id, run, name, beam, valve, guiding_coil_version, \
              guiding_coil_condition, measured_times, sf1_position, \
              sf2_position, sf1_frequency, sf1_current, sf1_amplitude, \
              sf2_frequency, sf2_current, sf2_amplitude from [{}]"
              .format(table04, table03))
    # update table04 with table02
    c.execute("Update[{}]set(N_ucn_gadget_time_offset_0, \
                             N_ucn_Nanosc_1_time_offset_0, \
                             N_ucn_Nanosc_2_time_offset_0, \
                             N_ucn_Gadget_time_offset_10, \
                             N_ucn_Nanosc_1_time_offset_10, \
                             N_ucn_Nanosc_2_time_offset_10, \
                             N_ucn_Gadget_time_offset_20, \
                             N_ucn_Nanosc_1_time_offset_20, \
                             N_ucn_Nanosc_2_time_offset_20) \
              =(select N_ucn_gadget_time_offset_0, \
                N_ucn_Nanosc_1_time_offset_0, \
                N_ucn_Nanosc_2_time_offset_0, \
                N_ucn_Gadget_time_offset_10, \
                N_ucn_Nanosc_1_time_offset_10, \
                N_ucn_Nanosc_2_time_offset_10, \
                N_ucn_Gadget_time_offset_20, \
                N_ucn_Nanosc_1_time_offset_20, \
                N_ucn_Nanosc_2_time_offset_20 \
                From[{}]where[{}].name=[{}].name)"
              .format(table04, table02, table04, table02))

    # update table04 with table01
    c.execute("Update[{}]set(start_time, stop_time, duration) \
              =(select start_time, stop_time, duration From[{}] \
              where[{}].name=[{}].name)".format(table04, table01,
                                                table04, table01))
    # two faster files are lost, so I got time info from root file and
    # add it to table04.
    # file1:NY_SF1_OFF_SF2_ON_7kHz_30cm_withoutGCv4 time info lost
    # file2:NY_SF1_OFF_SF2_ON_21kHz_20cm_withoutGCv4 time info lost
    c.execute("Update[{}]set duration=161 where \
              name='NY_SF1_OFF_SF2_ON_7kHz_30cm_withoutGCv4'".format(table04))
    c.execute("Update[{}]set duration=161 where \
              name='NY_SF1_OFF_SF2_ON_21kHz_20cm_withoutGCv4'".format(table04))

    conn.commit()
    conn.close()
    print("initialization_basic_data is success!")
