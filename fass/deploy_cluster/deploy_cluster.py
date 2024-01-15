import paramiko

# 包括安装 suzaku 集群，UI管理面，API

# 服务器列表
# servers = [
#     {
#         'hostname': 'server1.example.com',
#         'port': 22,
#         'username': 'root',
#         'password': 'password'
#     },
#     {
#         'hostname': 'server2.example.com',
#         'port': 22,
#         'username': 'root',
#         'password': 'password'
#     },
#     # 添加更多服务器...
# ]
# commands_env_init = ["","","",""]
# command_deploy_etcd = ""
# command_deploy_suzaku = ""
# command_deploy_web = ""
# command_deploy_api = ""
#
# # 执行Shell命令的函数,初始化集群环境
# def execute_command(server, command):
#     client = paramiko.SSHClient()
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 自动添加主机密钥
#     client.connect(server['hostname'], server['port'], server['username'], server['password'])
#     stdin, stdout, stderr = client.exec_command(command)
#     output = stdout.read().decode()
#     error = stderr.read().decode()
#     client.close()
#     return output, error
#
#
# # 遍历服务器列表，执行Shell命令
# for server in servers:
#     for command in commands_env_init:
#     #command = 'ls'  # 替换为要执行的Shell命令
#         output, error = execute_command(server, command)
#         print(f"Server: {server['hostname']}")
#         print(f"Command: {command}")
#         print(f"Output: {output}")
#         print(f"Error: {error}")
#         print()  # 换行分隔服务器输出
#
#
# def init_env(hostname,port,username,password,command):
#     #创建SSH客户端
#     client = paramiko.SSHClient()
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy)#自动添加主机名和主机密钥
#     try:
#         #连接服务器
#         client.connect(hostname,port,username,password)
#         #执行命令
#         stdin,stdout,stderr = client.exec_command(command)
#         output = stdout.read().decode() #读取命令输出
#         error  = stderr.read().decode() #读取命令错误输出
#         return output,error
#     except Exception as e:
#         print(f"Error:{e}")
#     finally:
#         #关闭连接
#         client.close()
#

def remote_exec(hostname, port, username, password, command):
    # 创建SSH客户端
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 自动添加主机名和主机密钥

    try:
        # 连接服务器
        client.connect(hostname, port, username, password)

        # 执行命令
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()  # 读取命令输出
        error = stderr.read().decode()  # 读取命令错误输出

        # 返回命令的输出和错误
        return output, error
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # 关闭连接
        client.close()

# 使用示例
hostname = "172.26.9.240"
port = 22  # 默认SSH端口是22
username = "root"
password = "111111"
command = "ls -l"  # 要执行的命令，例如列出目录内容
output, error = remote_exec(hostname, port, username, password, command)
if output:
    print("Output:", output)
if error:
    print("Error:", error)
