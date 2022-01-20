
import paramiko
import os

hostname = "119.28.224.75"
port = 22
username = "root"
password = "*2012xiaolzz"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname, port=port, username=username, password=password)

# 执行命令
# stdin, stdout, stderr = ssh.exec_command('df -hl')
# 结果放到stdout中，如果有错误将放到stderr中
# print(stdout.read().decode())

t = paramiko.Transport(hostname, port)
t.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(t)
local_dir = "D:/work_space/code/lock_step/client/game_card/Assets/StreamingAssets/Abs"
remote_dir = "/usr/share/nginx/download/Abs"

ssh.exec_command("mkdir -p {0}".format(remote_dir))

dir_entities = os.listdir(local_dir)
print("dir_entities", dir_entities)
for file in dir_entities:
    sftp.put(os.path.join(local_dir, file), os.path.join(remote_dir, file).replace("\\", "/"))

ssh.exec_command("chmod -R 755 {0}".format(remote_dir))

# 关闭连接
ssh.close()
sftp.close()
