import paramiko

#建立连接
transport = paramiko.Transport(('hr',22))
transport.connect(username='root',password='my@tfs2016$')

sftp = paramiko.SFTPClient.from_transport(transport)

#sftp.put('C:\InstallConfig.ini','/tmp/test.txt')

sftp.get('/tmp/test.txt','from_linux.txt')

transport.close()