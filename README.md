# AODI·Auto-obtain-dynamic-IP·自动获取动态公网地址

[![](https://github.com/linwhitehat/AODI/blob/master/svg/Home-L1n-brightgreen.svg)](https://github.com/linwhitehat/AODI) [![Python 3](https://github.com/linwhitehat/AODI/blob/master/svg/python-3-informational.svg "Python 3")](https://www.python.org/) [![MIT](https://github.com/linwhitehat/AODI/blob/master/svg/License-MIT-green.svg)](https://github.com/linwhitehat/AODI#%E4%BD%BF%E7%94%A8%E8%AE%B8%E5%8F%AF)

<p align="center">
  <a href="https://github.com/linwhitehat/AODI">中文</a> •
  <a href="https://github.com/linwhitehat/AODI/blob/master/README.en.md">English</a>
</p>


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

**注意**

配置信息中涉及个人敏感内容，**不要**在公开网络环境下留下任何个人的私密内容。

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
[AODI-GUIDE](https://linwhitehat.github.io/Blog/2020/06/18/%E5%AE%9A%E6%97%B6%E8%87%AA%E5%8A%A8%E8%8E%B7%E5%8F%96%E5%8A%A8%E6%80%81%E5%85%AC%E7%BD%91IP.html)

## 参与修订
非常欢迎你加入！你可以通过[提交issue](https://github.com/linwhitehat/AODI/issues/new)或pull请求参与贡献。

## 使用许可
[MIT](LICENSE) © linwhitehat