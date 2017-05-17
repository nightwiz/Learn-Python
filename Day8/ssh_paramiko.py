import paramiko

#创建SSH对象
ssh = paramiko.SSHClient()

#允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#连接服务器
ssh.connect(hostname='hr',port=22,username='root',password='my@tfs2016$')

#执行命令,stdout和stderr只有一个有结果，要么正确stdout，要么错误stderr
stdin,stdout,stderr = ssh.exec_command('df')

#获取结果
result = stdout.read()
print(result.decode())

#关闭连接
ssh.close()

