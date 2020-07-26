## 问题
1. 解压python的安装包到``/usr/local/src/python_setup``
2. 进入后``make && make install``
1. 装好的python3中没有pip3，安装pip3失败
3. 错误提示
> zipimport.ZipImportError: can't decompress data; zlib not available

## 解决过程
1. 这是缺少了zlib有关的组件
2. 查看``rpm -qa | fgrep zlib``，需要以下两个组件的支持
```
zlib-1.2.3-29.el6.x86_64
zlib-devel-1.2.3-29.el6.x86_64
```

3. 发现设备上只有zlib-1.2.3-29.el6.x86_64

4. ``yum -y install zlib*``

5. 装好后修改python安装包中Modules/Setup文件，就是``/usr/local/src/python_setup/Modules/Setup``这个文件
6. 如果忘记了就用``find / -name Setup``找
6. 修改这个文件，把``#zlib zlibmodule.c -I$(prefix)/include -L$(exec_prefix)/lib -lz``前面的注释去掉
7. 返回到python的安装包目录，``make && make install``
8. 提示``Fatal Python error: Py_Initialize: Unable to get the locale encoding``
9. 更改语系，``export LANG=zh_CN.utf-8``
10. ``make && make install``
11. 安装成功
