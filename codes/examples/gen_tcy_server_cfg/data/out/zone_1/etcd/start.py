# machine Machine
# etcd_cluster EtcdServerCluster
# etcd EtcdServer



import paramiko

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname="119.91.239.128", port="22", username="root", \
    pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))
shell = ssh_client.invoke_shell()


docker run -d --network my-network --name etcd_2 --mount type=volume,src=tcy_code,dst=/root/code --mount type=volume,src=tcy_build,dst=/root/build --mount type=volume,src=tcy_zone,dst=/root/zone --mount type=bind,src=/root/tmp,dst=/root/tmp  lxl_debian etcd


shell.sendall("ls -al\n")
shell.sendall("ret=$?\n")
shell.sendall("echo xxx $? $ret\n")
shell.sendall("exit $ret\n")
shell.shutdown_write()