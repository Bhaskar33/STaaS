#!/usr/bin/python
import os,sys,socket,commands,time,getpass

s_ip="192.168.122.211"
s_port=8888
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

drive_name=raw_input("enter storage drive name: ")
drive_space=raw_input("enter drive space you want: ")
s.sendto(drive_name,(s_ip,s_port))
s.sendto(drive_space,(s_ip,s_port))

res=s.recvfrom(100)

if res[0]=="done":
	os.system('mkdir /media/'+drive_name)
	os.system('mount '+s_ip+':/mnt/'+drive_name+' /media/'+drive_name)
else:
	print "Server not found!!"
