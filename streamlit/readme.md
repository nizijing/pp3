## 参考
https://docs.streamlit.io/


### 1. 安装
```bash
python3 -m venv .venv
source .venv/bin/activate

pip3 install --upgrade pip
pip3 install streamlit
pip3 install alibabacloud_schedulerx220190430==1.1.12
pip3 install matplotlib
pip3 install streamlit-authenticator

pip3 install -r requestments.txt
```

### 2. 准备环境变量
- ALIBABA_CLOUD_ACCESS_KEY_ID：阿里云AccessKey ID
- ALIBABA_CLOUD_ACCESS_KEY_SECRET：阿里云AccessKey Secret
- ORGANIZATIONID：云效中公司的ID

### 3. 准备配置文件
- 准备config.yaml，与devops.py同目录
- 内容类似如下
```yaml
credentials:
  usernames:
    zhangsan:
      email: zhangsan@shiyanjia.com
      logged_in: False # Will be managed automatically
      name: 张三
      password: abc # Will be hashed automatically
    lisi:
      email: lisi@shiyanjia.com
      logged_in: False # Will be managed automatically
      name: 李四
      password: def # Will be hashed automatically
cookie:
  expiry_days: 30
  key: some_signature_key # Must be string
  name: some_cookie_name
preauthorized:
  emails:
  - melsby@shiyanjia.com
```

### 4. 运行

```bash
source .venv/bin/activate
streamlit run devops.py --server.port 8092
```