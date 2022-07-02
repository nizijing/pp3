import xlwings as xw

app = xw.App(visible=False,add_book=False)
wb = app.books.open('1.xlsx')
ws = wb.sheets['Sheet1']
# 获取"AB2"单元格的行标和列标
print(ws.range('C2').row)
print(ws.range('C2').column)

# 高度和宽度
print(ws.range('C2').row_height)
print(ws.range('C2').column_width)

# 设置颜色,可根据RGB颜色表寻找自己想要的颜色
ws.range('C2').color = (255,0,0)

# 获取颜色
print(ws.range('C2').color)

# 清除颜色格式
ws.range('AB2').color = None

# 使用公式
ws.range('C2').formula='=SUM(A2,B2)'

# 另外还可以获取某一个单元格的公式
print(ws.range('C2').formula_array)

# 清除工作表的所有内容但是保留原有格式
# ws.clear_contents()
# 当然了还有很多其他的属性
#range.address        range.current_region    range.end
#range.api            range.autofit          range.expand

wb.save()
wb.close()
# 退出excel程序，
app.quit()