# add_argument() 方法（定义如何解析命令行参数）
# name or flags - 选项字符串的名字或者列表，例如 foo 或者 -f, --foo。
# action - 命令行遇到参数时的动作，默认值是 store。
# – store_const，表示赋值为const；
# – append，将遇到的值存储成列表，也就是如果参数重复则会保存多个值;
# – append_const，将参数规范中定义的一个值保存到一个列表；
# – count，存储遇到的次数；此外，也可以继承 argparse.Action 自定义参数解析；
# nargs - 应该读取的命令行参数个数，可以是
# 具体的数字，或者是?号，当不指定值时对于 Positional argument 使用 default，对于 Optional argument 使用 const
# 或者是 * 号，表示 0 或多个参数；
# 或者是 + 号表示 1 或多个参数。
# const - action 和 nargs 所需要的常量值。
# default - 不指定参数时的默认值。
# type - 命令行参数应该被转换成的类型。
# choices - 参数可允许的值的一个容器。
# required - 可选参数是否可以省略 (仅针对可选参数)。
# help - 参数的帮助信息，当指定为 argparse.SUPPRESS 时表示不显示该参数的帮助信息.
# metavar - 在 usage 说明中的参数名称，对于必选参数默认就是参数名称，对于可选参数默认是全大写的参数名称.
# dest - 解析后的参数名称，默认情况下，对于可选参数选取最长的名称，中划线转换为下划线.

import math
import argparse  # 1、导入argpase包


def parse_args():
    parse = argparse.ArgumentParser(description='Calculate cylinder volume')  # 2、创建参数对象
    parse.add_argument('-r', '--radius', default=2, type=int, metavar='', help='Radius of Cylinder')  # 3、往参数对象添加参数
    parse.add_argument('-H', '--height', default=4, type=int, metavar='', help='height of Cylinder')
    args = parse.parse_args()  # 4、解析参数对象获得解析对象
    return args


def cal_vol(radius, height):
    vol = math.pi * pow(radius, 2) * height
    return vol


if __name__ == '__main__':
    args = parse_args()
    print(cal_vol(args.radius, args.height))  # 5、使用解析对象.参数获取使用命令行参数



