# AODI·Auto-obtain-dynamic-IP

[![home](https://github.com/linwhitehat/AODI/blob/master/svg/Home-L1n-brightgreen.svg)](https://github.com/linwhitehat/AODI) [![Python 3](https://github.com/linwhitehat/AODI/blob/master/svg/python-3-informational.svg "Python 3")](https://www.python.org/)

<p align="center">
  <a href="https://github.com/linwhitehat/AODI">中文</a> •
  <a href="https://github.com/linwhitehat/AODI/blob/master/README.en.md">English</a>
</p>

## Background
AODI is a small tool developed based on the Python language. It can be used to regularly update the dynamically changing public network IP and push it to the mailbox to provide certain services for various remote services. Application scenarios such as remote control to connect to the PC at home, because you only need to know the public network IP of the current remote device, so reducing the use of DDNS deployment will appear flexible and light.

## Install & Configuration
### Install
``` shell
# Linux
git clone https://github.com/linwhitehat/AODI.git /root/rootcrons/
crontab /root/rootcrons/rootcron
/etc/init.d/cron restart
```
### Configuration
This project is developed using [python3](https://www.python.org/), the following libraries are required to support normal operation:

- [x] email
- [x] smtplib
- [x] requests
- [x] time
- [x] json
- [x] re

The basic configuration of the tool includes`e-mail config`、`Router config`and`headers`of`public IP config`，these are commented at the corresponding position of the code block.

**Notice**

The configuration information involves personal sensitive content. Please **DO NOT** leave any personal private content in the open network environment.

## Usage
Run directly under the command line (IDE) or customize timing use:
``` shell
# Run directly
python3 AODI.py

# Run regularly
vim /root/rootcrons/rootcron
0 * */1 * * /usr/bin/python /root/rootcrons/reportip.py
crontab /root/rootcrons/rootcron
/etc/init.d/cron restart
```

## GUIDE
[AODI-GUIDE](https://linwhitehat.github.io/Blog/2020/06/18/%E5%AE%9A%E6%97%B6%E8%87%AA%E5%8A%A8%E8%8E%B7%E5%8F%96%E5%8A%A8%E6%80%81%E5%85%AC%E7%BD%91IP.html)

## Contributing
Feel free to dive in!
[Open new issue](https://github.com/linwhitehat/AODI/issues/new) or submit PRs.

## License
[MIT](LICENSE) © linwhitehat