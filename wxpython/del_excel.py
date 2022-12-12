import wx
import xlwings as xw
import tkinter as tk
from tkinter import filedialog


def getFilePath():
    root = tk.Tk()
    root.withdraw()
    filepath = filedialog.askopenfilename()
    return filepath


def main():
    filepath = getFilePath()
    app=xw.App(visible=False,add_book=False) 
    wb=app.books.open(filepath)
    sheet = wb.sheets["报告"]
    data = {}
    pros = set()
    dates = set()

    for i in range(5, sheet.used_range.last_cell.row):
        user = sheet.range(i, 3).value
        pro = sheet.range(i, 4).value
        hour = sheet.range(i, 6).value
        date = sheet.range(i, 7).value
        dates.add(date)
        pros.add(pro)
        if user not in data:
            data[user] = {}
        if pro not in data[user]:
            data[user][pro] = {}
        data[user][pro][date] = hour

    sht_result_name = ''
    index = 0
    for _ in wb.sheets:
        sht_result_name = "result{}".format(index)
        sheet_names = [sheet.name for sheet in wb.sheets]
        if sht_result_name in sheet_names:
            index = index + 1
        else:
            break

    wb.sheets.add(sht_result_name)
    row = 1
    sht_result = wb.sheets[sht_result_name]
    sht_result.range(row,1).value = 'No'
    sht_result.range(row,2).value = '员工'
    sht_result.range(row,3).value = '项目'
    col = 3  # No, 员工， 项目
    date_dict = {}
    for date in sorted(dates):
        col += 1
        date_dict[date] = col
        sht_result.range(row, col).value = date[-5:]

    for user, projects in data.items():
        for pro, dates in projects.items():
            row = row + 1
            sht_result.range(row, 1).value = row -1
            sht_result.range(row, 2).value = user
            sht_result.range(row, 3).value = pro
            for date, hour in dates.items():
                sht_result.range(row, date_dict[date]).value = hour

    wb.save()
    wb.close()
    app.quit()

if __name__ == "__main__":
    main()