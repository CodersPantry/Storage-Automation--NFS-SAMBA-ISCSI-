import ping
import paramiko
def connection(host,user,passwd):
    if ping.test(host):
        try:
            client=paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(host,username=user,password=passwd)
            return 1
        except Exception as e:
            print(e)
            return 0
    else:
        return 0
