import re
import xlwt
from _mavLinkAnalyzing import mavLinkAnalyzing

file = open('MAVLink_20170908_1636.txt')
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
patternDOWN.pattern_fore_colour = 50
styleDOWN = xlwt.XFStyle()
styleDOWN.pattern = patternDOWN
styleDOWN.borders = borders
styleDOWN.alignment = alignment

patternUP = xlwt.Pattern()
patternUP.pattern = 1
patternUP.pattern_fore_colour = 41
styleUP = xlwt.XFStyle()
styleUP.pattern = patternUP
styleUP.borders = borders
styleUP.alignment = alignment

b = 0
index = 0
for line in file:
    flag = False
    if line.startswith('s32FrameLen'):
        print('DOWN')
        direction = 'DOWN'
        flag = True
    elif line.startswith('PC back '):
        print('UP')
        direction = 'UP'
        flag = True

    if flag:
        index += 1
        lList = re.findall(r"\b\d+\b",line)
        if lList:
            l = int(lList[0])
            print(l)

        data = file.readline()
        message = data.split()
        print(message)

        ml = mavLinkAnalyzing(message)

        messageID = ml.getMessageID()

        description = ml.getDescription()

        messageStr = ml.getDataStr()

        


        
        if direction == 'DOWN':
            style = styleDOWN
        else:
            style = styleUP
        

        row = index
        # index
        sheet.write(row,0,index,style)
        
        # direction
        sheet.write(row,1,direction,style)
        
        # messageID
        sheet.write(row,2,'#'+str(messageID),style)
        
        # description
        sheet.write(row,3,description,style)
        
        # message
        sheet.write(row,4,messageStr,style)

        if index > 10000:
            break


print(index)
input()

xls.save('MAVLink_20170908_1636.xls')
