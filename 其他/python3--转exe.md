[参考链接](https://blog.csdn.net/yufen9987/article/details/73865281)

#### 安装
```
pip install pyinstaller
```

找到你的python3版本(我的是3.7.2-64位)   
[下载地址](https://sourceforge.net/projects/pywin32/files/pywin32/Build%20221/)


#### 用法
```
D:\11zijing\python3\excel_sum>pyinstaller -F excelsum.py
```

倒数第2行告诉你exe位置
```
112 INFO: PyInstaller: 3.5
113 INFO: Python: 3.7.2
115 INFO: Platform: Windows-10-10.0.17134-SP0
120 INFO: wrote D:\11zijing\python3\excel_sum\excelsum.spec
130 INFO: UPX is not available.
133 INFO: Extending PYTHONPATH with paths
['D:\\11zijing\\python3\\excel_sum', 'D:\\11zijing\\python3\\excel_sum']
134 INFO: checking Analysis
139 INFO: Building Analysis because Analysis-00.toc is non existent
140 INFO: Initializing module dependency graph...
151 INFO: Initializing module graph hooks...
153 INFO: Analyzing base_library.zip ...
2960 INFO: running Analysis Analysis-00.toc
2970 INFO: Adding Microsoft.Windows.Common-Controls to dependent assemblies of final executable
  required by d:\program files (x86)\python3\python.exe
3419 INFO: Caching module hooks...
3424 INFO: Analyzing D:\11zijing\python3\excel_sum\excelsum.py
4155 INFO: Loading module hooks...
4155 INFO: Loading module hook "hook-encodings.py"...
4339 INFO: Loading module hook "hook-lxml.etree.py"...
4340 INFO: Loading module hook "hook-pydoc.py"...
4342 INFO: Loading module hook "hook-xml.etree.cElementTree.py"...
4345 INFO: Loading module hook "hook-xml.py"...
4550 INFO: Looking for ctypes DLLs
4551 INFO: Analyzing run-time hooks ...
4557 INFO: Looking for dynamic libraries
4787 INFO: Looking for eggs
4787 INFO: Using Python library d:\program files (x86)\python3\python37.dll
4789 INFO: Found binding redirects:
[]
4793 INFO: Warnings written to D:\11zijing\python3\excel_sum\build\excelsum\warn-excelsum.txt
4826 INFO: Graph cross-reference written to D:\11zijing\python3\excel_sum\build\excelsum\xref-excelsum.html
4859 INFO: checking PYZ
4860 INFO: Building PYZ because PYZ-00.toc is non existent
4862 INFO: Building PYZ (ZlibArchive) D:\11zijing\python3\excel_sum\build\excelsum\PYZ-00.pyz
5454 INFO: Building PYZ (ZlibArchive) D:\11zijing\python3\excel_sum\build\excelsum\PYZ-00.pyz completed successfully.
5466 INFO: checking PKG
5467 INFO: Building PKG because PKG-00.toc is non existent
5467 INFO: Building PKG (CArchive) PKG-00.pkg
14930 INFO: Building PKG (CArchive) PKG-00.pkg completed successfully.
14933 INFO: Bootloader d:\program files (x86)\python3\lib\site-packages\PyInstaller\bootloader\Windows-64bit\run.exe
14933 INFO: checking EXE
14937 INFO: Building EXE because EXE-00.toc is non existent
14937 INFO: Building EXE from EXE-00.toc
14938 INFO: Appending archive to EXE D:\11zijing\python3\excel_sum\dist\excelsum.exe
14948 INFO: Building EXE from EXE-00.toc completed successfully.
```