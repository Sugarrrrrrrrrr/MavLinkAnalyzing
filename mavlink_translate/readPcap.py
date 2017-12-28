import xlwt


if __name__ == '__main__':
    
    with open('.cfg', 'r') as f:
        for line in f:
            if line.startswith('<StatusCenter>'):
                line = f.readline().strip()
                import sys
                sys.path.append(line)
                from parse import mavutil

    file_name = 'Wireshar1'

    mf = mavutil.mavlink_connection(file_name + '.pcap', ip_list=['192.168.1.7'])
    

    xls = xlwt.Workbook()
    sheet = xls.add_sheet('sample')

    borders = xlwt.Borders()
    borders.left = 1
    borders.right = 1
    borders.top = 1
    borders.bottom = 1
    borders.left_colour = 1
    borders.right_colour = 1
    borders.top_colour = 1
    borders.bottom_colour = 1

    alignment = xlwt.Alignment()
    alignment.horz = 1
    alignment.vert = 1

    patternDOWN = xlwt.Pattern()
    patternDOWN.pattern = 1
    patternDOWN.pattern_fore_colour = 26
    styleDOWN = xlwt.XFStyle()
    styleDOWN.pattern = patternDOWN
    styleDOWN.borders = borders
    styleDOWN.alignment = alignment

    patternUP = xlwt.Pattern()
    patternUP.pattern = 1
    patternUP.pattern_fore_colour = 27
    styleUP = xlwt.XFStyle()
    styleUP.pattern = patternUP
    styleUP.borders = borders
    styleUP.alignment = alignment

    styleUNKNOW = xlwt.Pattern()

    index = 0
    m = mf.recv_msg()
    for i in range(100000):
        
        if m.get_type() == 'BAD_DATA':
            try:
                m = mf.recv_msg()
            except Exception as e:
                print(e)
            continue

        print('【%4d】:' % i, '【%4d】' % m.get_srcSystem(), m)
        index += 1

        if m.get_srcSystem() == 1:
            direction = 'DOWN'
        elif m.get_srcSystem() == 255:
            direction = 'UP'
        else:
            # print('unknow srcSystem:%d' % m.get_srcSystem())
            direction = 'UNKNOW'

        messageID = m.get_msgId()
        description = str(m)
        messageStr = m.get_msgbuf().hex().upper()

        if direction == 'DOWN':
            style = styleDOWN
        elif direction == 'UP': 
            style = styleUP
        else:
            # input('unknow srcSystem:%d'% m.get_srcSystem())
            style = styleUNKNOW


        row = index
        # index
        sheet.write(row,0,index,style)
        
        # direction
        sheet.write(row,1,direction,style)
        
        # messageID
        sheet.write(row,2,'#'+ str(messageID),style)
        
        # description
        sheet.write(row,3,description,style)
        
        # message
        sheet.write(row,4,messageStr,style)
        


        #end for
        try:
            m = mf.recv_msg()
        except Exception as e:
            print(e)
            break

    print('index:', index)
    input()

    xls.save(file_name + '.xls')
