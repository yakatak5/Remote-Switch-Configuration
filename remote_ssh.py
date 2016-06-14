#!/usr/bin/python
#!python

import paramiko
import sys
import json
import pdb

class device() :


	def __init__( self, ip, user, pwd):
		self.ip = ip  #ip address
		self.user = user #username
		self.pwd = pwd #pasword

	def login(self):
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy())
		ssh.connect(self.ip , username= self.user, password= self.pwd)
		#SSH into device

    

	def OSPF(self, intr, ins, ip, area):
    	
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(self.ip, 22, self.user, self.pwd, look_for_keys=False, timeout=5)
		stdin,stdout,stderr = ssh.exec_command('conf t ; feature ospf ; int ' + intr + ' ; ip address ' + ip + ' ; ip router ospf ' + ins + ' area ' + area + ' ; copy run start')
		print json.dumps (stdout.readlines(), indent = 3)

		#configures ospf

	def cmd(self, command):
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(self.ip, 22, self.user, self.pwd, look_for_keys=False, timeout=5)
		stdin,stdout,stderr = ssh.exec_command( command )
		print json.dumps (stdout.readlines(), indent = 3)
		#send command and print output

	def EIGRP(self, intr, AS, ins, ip):
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(self.ip, 22, self.user, self.pwd, look_for_keys=False, timeout=5)
		stdin,stdout,stderr = ssh.exec_command('conf t ; feature eigrp ; router eigrp ' + AS +' ; int ' + intr +  ' ; ip address ' + ip + ' ; ip router eigrp ' + ins + ' ; copy run start')
		print json.dumps (stdout.readlines(), indent = 3)

		#configures eigrp











if __name__=='__main__':

	




