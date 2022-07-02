import xlwings as xw

wb = xw.Book()
wb.save('2.xlsx')

sheet1 = wb.sheets["sheet1"]
# 或者
# sheet1 =xw.books['1.xlsx'].sheets['sheet1']
sheet1.range('F1').value = 'F1'
sheet1.range('G1').value = [['a','b','c'], [1,2,3]]

# 删除
# sheet1.range('A1').clear()

# 当然也可以将pandas的DataFrame数据写入
import pandas as pd
df = pd.DataFrame([[1,2], [3,4]], columns=['A', 'B'])
sheet1.range('A1').value = df
# 读取数据，输出类型为DataFrame
sheet1.range('A1').options(pd.DataFrame, expand='table').value
wb.save('2.xlsx')
wb.close()