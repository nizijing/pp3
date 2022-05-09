import xlwings as xw
app=xw.App(visible=True,add_book=False)
#不显示Excel消息框
app.display_alerts=False 
#关闭屏幕更新,可加快宏的执行速度
app.screen_updating=False  
wb=app.books.open('1.xlsx')
# 输出打开的excle的绝对路径
print(wb.fullname)
wb.save()
wb.close()
# 退出excel程序，
app.quit()
# 通过杀掉进程强制Excel app退出
# app.kill() 
# 以第一种方式创建Book时，打开文件的操作可如下
wb = xw.Book('1.xlsx')