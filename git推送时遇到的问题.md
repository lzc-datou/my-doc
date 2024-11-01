# git推送时遇到的问题

##### 1. git push -u origin main fatal: unable to access 'https://github.com/lzc-datou/Uav-systems-engineering-and-application.git/': Failed to connect to github.com port 443 after 21095 ms: Couldn't connect to server
首先端口443明确用于HTTPS服务，因此是HTTPS（加密）流量的标准端口。它也称为HTTPS端口443。出现此问题是使用了代理使得HTTPS端口发生了变化，导致连接失败。
**解决方法：** 将git使用的https端口改为代理使用的端口（打开代理软件自行查询其设置的端口）。
```bash
# 设置端口
git config --global http.proxy 127.0.0.1:7899
git config --global https.proxy 127.0.0.1:7899
# 取消端口设置
git config --global --unset http.proxy
git config --global --unset https.proxy
```
