import xlwt

xls = xlwt.Workbook()
sheet = xls.add_sheet('sample')
sheet.write(0,0,'netcom111')
sheet.write(0,1,'conw.net')
xls.save('sample.xls')

