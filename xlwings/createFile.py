import xlwings as xw


# 方法1：
# 创建一个新的App，并在新App中新建一个Book
def way1():
    wb = xw.Book()
    wb.save('1.xlsx')
    wb.close()


# 方法2：
# 当前App下新建一个Book
# visible参数控制创建文件时可见的属性
def way2():
    app=xw.App(visible=False,add_book=False)
    wb=app.books.add()
    wb.save('2.xlsx')
    wb.close()
    #结束进程
    app.quit()

if __name__ == '__main__':
    way1()
    way2()
