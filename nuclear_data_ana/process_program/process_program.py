"""This module's docstring summary line.
create tables under different SF conditions.
"""
from process_program.global_env.read import A
from process_program.global_env.basic_fun import get_cursor, drop_table, create_table
from process_program.global_env.all_tables import create_table11_sql, \
                                                  create_table12_sql, \
                                                  create_table13_sql, \
                                                  create_table14_sql, \
                                                  create_table15_sql, \
                                                  create_table16_sql



def update_with_background(conn, table11, table12):
    """ used to subtract the background contribution.
    """
    c = get_cursor(conn)
    y12_temp = []
    y11 = c.execute("select name, N_ucn_gadget_time_offset_0, \
                    N_ucn_Gadget_time_offset_10, \
                    N_ucn_Gadget_time_offset_20, \
                    N_ucn_Nanosc_1_time_offset_0, \
                    N_ucn_Nanosc_2_time_offset_0, \
                    N_ucn_Nanosc_1_time_offset_10, \
                    N_ucn_Nanosc_2_time_offset_10, \
                    N_ucn_Nanosc_1_time_offset_20, \
                    N_ucn_Nanosc_2_time_offset_20, \
                    duration From[{}]".format(table11)).fetchall()
    y12 = c.execute("select name, N_ucn_gadget_time_offset_0, \
                    N_ucn_Gadget_time_offset_10, \
                    N_ucn_Gadget_time_offset_20, \
                    N_ucn_Nanosc_1_time_offset_0, \
                    N_ucn_Nanosc_2_time_offset_0, \
                    N_ucn_Nanosc_1_time_offset_10, \
                    N_ucn_Nanosc_2_time_offset_10, \
                    N_ucn_Nanosc_1_time_offset_20, \
                    N_ucn_Nanosc_2_time_offset_20, \
                    duration From[{}]".format(table12)).fetchall()
    # subtract the background contribution
    for i in range(len(y12)):
        y12_temp.append((y12[i][1]-y11[0][1]*y12[i][10]/y11[0][10],
                         y12[i][2]-y11[0][2]*y12[i][10]/y11[0][10],
                         y12[i][3]-y11[0][3]*y12[i][10]/y11[0][10],
                         y12[i][4]-y11[0][4]*y12[i][10]/y11[0][10],
                         y12[i][5]-y11[0][5]*y12[i][10]/y11[0][10],
                         y12[i][6]-y11[0][6]*y12[i][10]/y11[0][10],
                         y12[i][7]-y11[0][7]*y12[i][10]/y11[0][10],
                         y12[i][8]-y11[0][8]*y12[i][10]/y11[0][10],
                         y12[i][9]-y11[0][9]*y12[i][10]/y11[0][10],
                         y12[i][0]))
    # update experiment data again
    c.executemany("Update[{}]set N_ucn_gadget_time_offset_0= ?, \
                  N_ucn_Gadget_time_offset_10= ?, \
                  N_ucn_Gadget_time_offset_20= ?, \
                  N_ucn_Nanosc_1_time_offset_0= ?, \
                  N_ucn_Nanosc_2_time_offset_0= ?, \
                  N_ucn_Nanosc_1_time_offset_10= ?, \
                  N_ucn_Nanosc_2_time_offset_10= ?, \
                  N_ucn_Nanosc_1_time_offset_20= ?, \
                  N_ucn_Nanosc_2_time_offset_20= ? \
                  where name= ?".format(table12), y12_temp)


def process_program(conn, table04, table11, table12, table13,
                    table14, table15, table16):
    """process program is used to get the table under the different SF conditions.
    """
    c = get_cursor(conn)
    c.execute('''ATTACH[{}]as AM '''.format(A.DB_FILE_1))

    drop_table(conn, table11)
    drop_table(conn, table12)
    drop_table(conn, table13)
    drop_table(conn, table14)
    drop_table(conn, table15)
    drop_table(conn, table16)

    # create table11
    create_table(conn, create_table11_sql)
    c.execute('Insert into[{}]select * FROM AM.[{}] WHERE beam = ? or valve = ?'
              .format(table11, table04), [("off"), ("off")])
    # create table12
    create_table(conn, create_table12_sql)
    c.execute('Insert into[{}]select * FROM AM.[{}] WHERE beam= ? and valve= ?'
              .format(table12, table04), [("on"), ("on")])
    # update table12 with background correction
    update_with_background(conn, table11, table12)
    # create table13
    create_table(conn, create_table13_sql)
    c.execute('Insert into[{}]select * FROM[{}]WHERE sf1_frequency= ? and \
              sf2_frequency= ?'.format(table13, table12), [(0), (0)])
    # create table14
    create_table(conn, create_table14_sql)
    c.execute('Insert into[{}]select * FROM[{}]WHERE sf1_frequency != ? and \
              sf2_frequency= ?'.format(table14, table12), [(0), (0)])
    # create table15
    create_table(conn, create_table15_sql)
    c.execute('Insert into[{}]select * FROM[{}]WHERE sf1_frequency= ? and \
              sf2_frequency != ?'.format(table15, table12), [(0), (0)])
    # create table16
    create_table(conn, create_table16_sql)
    c.execute('Insert into[{}]select * FROM[{}]WHERE sf1_frequency != ? and \
              sf2_frequency != ?'.format(table16, table12), [(0), (0)])
    c.execute("DETACH DATABASE 'AM'")
    conn.commit()
    conn.close()
    print("process part is achieved!")
