import ping
import paramiko
def pssh(host,username,password):
    if ping.test(host):
        print("success")
    else:
        print('host not reachable')
        h=input("Input exit to quit")
        if h.lower()=='exit':
            print('Bye')
        else:
            pssh(host,username,password)
pssh('192.168.5.129','root','redhat')
