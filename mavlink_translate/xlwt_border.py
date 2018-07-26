import xlwt

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')

for i in range(0,13):
    for j in range(0,40):
        border = xlwt.Borders()
        border.left = i
        border.left_colour = j

        style = xlwt.XFStyle()
        style.borders = border

        worksheet.write(i,j,str(i)+','+str(j),style)

workbook.save('xls_border.xls')
