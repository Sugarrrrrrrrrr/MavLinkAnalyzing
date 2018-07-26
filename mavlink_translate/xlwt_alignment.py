import xlwt

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')

for i in range(0,8):
    for j in range(0,5):
        alignment = xlwt.Alignment()
        alignment.horz = i
        alignment.vert = j

        style = xlwt.XFStyle()
        style.alignment = alignment

        worksheet.write(i,j,str(i)+','+str(j),style)

workbook.save('xls_alignment.xls')
