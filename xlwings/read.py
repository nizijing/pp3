import xlwings as xw

app = xw.App(visible=False,add_book=False)
wb = app.books.open('1.xlsx')
range_1 = wb.sheets[0].range('A1:D3')
print(range_1)

# <Range [1.xlsx]Sheet1!$A$1:$D$3>
print(range_1.value)
# [[None, 'a', 'b', None], [0.0, 1.0, 2.0, None], [1.0, 3.0, 4.0, None]]
# 切片方式
range_2 = wb.sheets[0][:3, :3]
# <Range [1.xlsx]Sheet1!$A$1:$C$3>

ws = wb.sheets['Sheet1']
shape = ws.used_range.shape
print(shape) #(2, 3)

nrow1 = ws.api.UsedRange.Rows.count
ncol1 = ws.api.UsedRange.Columns.count
print(nrow1) # 2
print(ncol1) # 3

rng = ws.range('A1').expand()
nrow2 = rng.last_cell.row
ncol2 = rng.last_cell.column
print(nrow2)  # 3
print(ncol2)  # 1

# 写值的情况
# 使用列表将1,2,3,4写入A1,A2,A3,A4
# transpose=True进行转置写入
wb.sheets[0].range('A1').options(transpose=True).value=[1,2,3,4]
# 将二维数组，储存在A1:B3中
wb.sheets[0].range('A1').options(expand='table').value=[[1,2],[3,4],[5,6]]
wb.save('3.xlsx')
wb.close()