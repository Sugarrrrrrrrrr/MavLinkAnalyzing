import xlwt

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')

for i in range(0,100):
    for j in range(0,40):
        pattern = xlwt.Pattern()
        pattern.pattern_fore_colour = i
        pattern.pattern = j

        style = xlwt.XFStyle()
        style.pattern = pattern

        worksheet.write(i,j,str(i)+','+str(j),style)

workbook.save('xls_color.xls')
