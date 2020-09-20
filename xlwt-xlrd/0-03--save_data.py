#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-09-20 14:13:21
# Author : zijing (zijing412@163.com)
###################################################
import xlwt

# 1. 获取工作簿
# 2. 在工作簿上建立sheet表
# 3. 设置sheet表格式
# 4. 向sheet表写入数据
# 5. 保存工作簿

# 获取工作簿
def get_save_wbk():
    try:
        wbk = xlwt.Workbook(encoding='utf-8')
        style = xlwt.XFStyle()
        fnt = xlwt.Font()
        fnt.name = u'宋体'
        style.font = fnt
        return wbk
    except Exception as err:
        print(str(err))
        exit


def set_sht_style(sht):
    # 1个宋体汉字 = 256 * 2
    sht.col(0).width = 256 * 5
    sht.col(1).width = 256 * 7
    sht.col(2).width = 256 * 12

    sht.write(0, 0, '编号')
    sht.write(0, 1, '姓名')
    sht.write(0, 2, '手机')

def main_save2excel(save_cont, savepath = 'result.xls'):
    wbk = get_save_wbk()
    sht = wbk.add_sheet('sheet_name', cell_overwrite_ok=True)
    set_sht_style(sht)
    i = 1

    for line in save_cont:
        sht.write(i, 0, line[0])
        sht.write(i, 1, line[1])
        sht.write(i, 2, line[2])
        i += 1
            
    wbk.save(savepath)

if __name__ == '__main__':
    test_data = [
        [1, '张三', '11122223333'],
        [2, '李四', '44455556666']
    ]
