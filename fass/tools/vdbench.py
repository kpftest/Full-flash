import os
import subprocess
import paramiko

client_ips = "xxxx,xxxx,xxxx"
#配置vdbench 文件
def conf():
    vdbench_home="/home/vdbench50406"
    threads=32
    wd="wd=wd1,sd=sd*,seekpct=0,rdpct=0,xfersize=1024k\n"
    rd="rd=rd1,wd=wd1,iorate=max,elapse=604800000,maxdata=400000G,interval=1,warmup=1\n"
    cont=[]
    hds=[]
    port=22
    username="root"
    password="password"
    sd_num=1

    hd="hd=default,vdbench={0},user=root,shell=ssh\n".format(vdbench_home)
    cont.append(hd)

    # f=open("ip.list")
    for host in client_ips:
        hd = host.split('.')[-1]
        system=("hd=hd{0},system={1}\n").format(hd.strip('\n'),host.strip('\n'))
        cont.append(system)
        hds.append(hd)

    # file=open("ip.list")
    for hostname in client_ips:
        hd = hostname.split('.')[-1]
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname, port, username, password)
        stdin,stdout,sterr = s.exec_command("ls -al /dev/disk/by-path/*|grep iscsi|awk '{print $9}'")
        luns = stdout.readlines()
        for lun in luns:
            sd="sd=sd{0},hd=hd{1},lun={2},threads={3},openflags=o_direct\n".format(sd_num,hd.strip('\n'),lun.strip('\n'),threads)
            cont.append(sd)
            sd_num=sd_num+1
        s.close()
    # file.close()

    cont.append(wd)
    cont.append(rd)

    with open(r"vdbench_parm","w+") as f:
        for line in cont:
            f.write(line)
    print("vdbench script path:"+os.getcwd()+"/vdbench_parm")

def exe():
    ip = client_ips[1]
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    s.connect(hostname="",port="",username="",password="")
    stdin,stdout,stderr = s.exec_command("")

def check():
    ip = client_ips[1]
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    s.connect(hostname="", port="", username="", password="")
    stdin, stdout, stderr = s.exec_command("")

