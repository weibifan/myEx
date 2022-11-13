### 2022-11-12  实验室的阿里云ECS   47.105.158.15

加载数据盘

cat /proc/version
Linux version 5.4.0-125-generic (buildd@lcy02-amd64-083) (gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.1)) #141-Ubuntu SMP Wed Aug 10 13:42:03 UTC 2022

fdisk -l  
发现有vda和vdb两个盘

df
发现只有vda

ls /home 发现是空的。
mount /dev/vdb1 /home  将磁盘挂载到/home下

root@iZm5ebjiawhqzdj6l27i5eZ:~# df
Filesystem     1K-blocks    Used Available Use% Mounted on
udev             8167108       0   8167108   0% /dev
tmpfs            1639348     700   1638648   1% /run
/dev/vda1       51420984 2883384  46214524   6% /
tmpfs            8196724       0   8196724   0% /dev/shm
tmpfs               5120       0      5120   0% /run/lock
tmpfs            8196724       0   8196724   0% /sys/fs/cgroup
tmpfs            1639344       0   1639344   0% /run/user/0
/dev/vdb1      515858104 5163268 484480488   2% /home

增加用户：
cat  /etc/group  查看有哪些组，选择users组   
cat /etc/passwd 看用户

useradd worker -m
ls /home

passwd worker
123@xjtu

配置用户：未做
为用户“myname”赋予sudo能能. vim /etc/sudoers 输入:wq 保存并退出,如果这时提示文件为readonly,重新输入:!wq

### 2022-11-13  安装宝塔管理系统，只能从纯净系统开始安装。https://www.bt.cn/new/download.html
上到网站，获得安装命令：
wget -O install.sh http://download.bt.cn/install/install-ubuntu_6.0.sh && sudo bash install.sh ed8484bec

根据安装结束的提示（如上）在阿里云控制台配置端口。使用tcp，在百度中搜索细节或阅读宝塔手册。

在阿里云控制台生成秘钥和公钥：

cat ~/.ssh/authorized_keys 
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCCMT6IqjB4QxLAkp0Vl/MUluwMOGbknbf7V+7whLUqdTzHpTafxhJ0pJp6CMwkXjPdpUoLVW/dkr2fyiW17psovq4hZ85SZCIjppIWIYmN+rbawCyHUYpl/pkAvTO9iBZMpkuhyJsZKwcibyh5+JaRULd59U1YwjKDFR9wLnm4lmoN6zM1fiL9TJsWtSHO3HUtVlLk5R/fdMtunKBQCfApgGQQ39UTEJTOpPRmNOGk2E6qXUbRnVkArLHr048MkEO+w/JiOgFja7A2ixXT2+VJGBxSxQ5p7m7KbjZgpVbG8kTST2QVroZe2Vs2RaCIbcREnmDITSEMc7ql/v7OLWLF skp-m5egzr4bvtofutw9odgx
