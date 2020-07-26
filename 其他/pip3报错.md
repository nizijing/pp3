## 信息
- Contos7
- 2.6.32-573.12.1.el6.x86_64
- python3.7.3

- ``pip3 install lxml``，提示以下错误
```
pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
```

- 在python3的脚本中执行``import ssl``提示
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/python3/lib/python3.7/ssl.py", line 98, in <module>
    import _ssl             # if we can't import it, let the error propagate
ModuleNotFoundError: No module named '_ssl'
```

- 其实早在``make``的时候就有报错了
```
Could not build the ssl module!
Python requires an OpenSSL 1.0.2 or 1.1 compatible libssl with X509_VERIFY_PARAM_set1_host().
LibreSSL 2.6.4 and earlier do not provide the necessary APIs, https://github.com/libressl-portable/portable/issues/381
```
## 解决过程
### 一般解决方法
- 先装一下依赖包

```
sudo yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite sqlite-devel readline-devel tk tk-devel gdbm gdbm-devel db4-devel libpcap-devel lzma xz xz-devel libuuid-devel libffi-devel
```

### 依旧报错
[参考链接](https://blog.csdn.net/devalone/article/details/82459276)

```
tar -zxvf libressl-2.7.4.tar.gz
cd libressl-2.7.4
./configure --prefix=/usr/local
make
sudo make install

echo '/usr/local/lib' >> /etc/ld.so.conf.d/local.conf 

sudo ldconfig -v
openssl version
# 显示LibreSSL 2.7.4

#4. 安装 libressl 代替openssl-devel
#回到 Python-3.7.0 目录，vim Modules/Setup
#删除有关 ssl 编译代码的注释，共 4 行，并修改 SSL 目录为 SSL=/usr/local, 如下所示:

# Socket module helper for SSL support; you must comment out the other
# socket line above, and possibly edit the SSL variable:
SSL=/usr/local
_ssl _ssl.c \
 -DUSE_SSL -I$(SSL)/include -I$(SSL)/include/openssl \
 -L$(SSL)/lib -lssl -lcrypto

#重新配置、编译：
./configure --prefix=/usr
make
```

- 按他提供的方法，到``make``这一步时，又报错了
```
./Modules/_ssl.c:70:6: error: #error "LibreSSL is missing X509_VERIFY_PARAM_set1_host(), see https://github.com/libressl-portable/portable/issues/381"
```

### 继续搜索
[参考连接](https://segmentfault.com/q/1010000015781670)

- 终于在这条参考链接的帮助下，成功了
- 关键点在于编译命令
- ``./config --prefix=/usr --openssldir=/usr/openssl shared zlib``
- 回到python3的安装目录，``make``就不再报错了

