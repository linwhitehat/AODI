# AODI·Auto-obtain-dynamic-IP

[![](https://img.shields.io/badge/Home-L1n-brightgreen.svg?logo=home-assistant)](https://github.com/linwhitehat/AODI) [![Python 3](https://img.shields.io/badge/python-3.7-informational.svg?logo=python "Python 3")](https://www.python.org/)

## 背景
AODI是一个基于python语言开发的小工具，可用于定时更新动态变化的公网IP并推送到邮箱，为多种远程服务提供一定服务，我的应用场景比如远程控制连接，因为只需要知道当前设备的公网IP即可，减少使用DDNS部署，灵活轻便。

## 安装&配置
### 安装
``` shell
# Linux
git clone https://github.com/linwhitehat/AODI.git /root/rootcrons/
crontab /root/rootcrons/rootcron
/etc/init.d/cron restart
```
### 配置
本项目使用[python3](https://www.python.org/)，需要使用以下库以支持正常运行：

- [x] email
- [x] smtplib
- [x] requests
- [x] time
- [x] json
- [x] re

工具基本配置包括`e-mail config`、`Router config`以及`public IP config`中的`headers`部分，在代码块位置均有注释。
**注意**配置信息中设及个人敏感内容，**不要**在公开网络环境下留下任何个人的私密内容。

## 使用
直接在命令行或IDE下运行或自定义定时使用：
``` shell
# Run directly
python3 AODI.py
# Run regularly
vim /root/rootcrons/rootcron
0 * */1 * * /usr/bin/python /root/rootcrons/reportip.py
crontab /root/rootcrons/rootcron
/etc/init.d/cron restart
```

## 教程
[AODI-GUIDE]()

## 参与修订
非常欢迎你加入！你可以通过[提交issue](https://github.com/linwhitehat/AODI/issues/new)或pull请求参与贡献。

## 使用许可
[MIT](LICENSE) © Richard Littauer