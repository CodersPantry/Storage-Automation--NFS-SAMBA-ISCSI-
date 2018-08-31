from sys import platform
from subprocess import getoutput
def test(Host='127.0.0.1'):
    OS=platform
    if 'win' in OS.lower():
        cmd="ping -n 2 {}".format(Host)
        output=getoutput(cmd)
        if 'bytes=32' in output:
            return 1
        else:
            return 0
    elif 'linux' in OS.lower():
        cmd="ping -c 2 {}".format(Host)
        output=getoutput(cmd)
        if 'bytes=32' in output:
            return 1
        else:
            return 0

