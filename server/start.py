#!/usr/bin/python
import os,commands,sys,socket,time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",8888))

while True:
	#taking name of drive from user
	data=s.recvfrom(100)
	d_name=data[0]

	#taking size of drive that user wants
	data1=s.recvfrom(100)
	d_size=data1[0]

	c_addr=data1[1][0]

	#creating LVM by the name of client drive
	os.system('lvcreate --name '+d_name+' --size '+d_size+'M xyz')

	#now we are formatting client's drive with xfs
	os.system('mkfs.xfs /dev/xyz/'+d_name)

	#now creating mount point 
	os.system('mkdir /mnt/'+d_name)

	#now mounting drive locally
	os.system('mount /dev/xyz/'+d_name+' /mnt/'+d_name)

	#now establish NFS-server configuration
	#os.system('yum install nfs-utils -y')

	#making entry in export file
	entry="/mnt/"+d_name+" "+c_addr+"(rw,no_root_squash)"

	#Appending to exports file
	f=open('/etc/exports','a')
	f.write(entry)
	f.write("\n")
	f.close()

	#now starting NFS-service persistent
	x=os.system('exportfs -r')
	
	if x== 0:
		s.sendto("done",data[1])
	else:
		print "check your code"
