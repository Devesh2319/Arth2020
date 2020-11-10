import os
import sys
import json
import subprocess
#AWS menu
def menu_AWS():
    ch=0
    while ch != 5:    
        print("\t\t\tWelcome to my Menu !!")
        print("\t\t\t*********************")
        print("\n")
        print("""          
              \t\t\t1=To Launch an Instance
              \t\t\t2=List the instance ids of all running instances
              \t\t\t3=To create an EBS volume 
              \t\t\t4=Attach EBS Volume to an instance
              \t\t\t5=exit
              """
              )
        ch= int(input("Enter your Choice : "))
        ou1=""
        x=0
        if ch==1:
            s=[["ami-0e306788ff2473ccb"],
               ["ami-052c08d70def0ac62"]]
            k=input("Enter name of key pair to be created : ")
            stkey="aws ec2 create-key-pair --key-name "+k+" --query 'KeyMaterial' --output text > "+k+".pem"
            os.system(stkey)
            sg=input("Enter name of security group to be created : ")
            sgc="aws ec2 create-security-group --group-name "+sg+" --description os1"
            ou1=subprocess.getoutput(sgc)
            eol=len(ou1)-3
            fsgid=ou1[18:eol]
            print(fsgid)
            print("""
                  1=Amazon Linux 2 AMI (HVM), SSD Volume Type - ami-0e306788ff2473ccb (64-bit x86) / ami-001e484a60bb07f8d (64-bit Arm)
                  2=Red Hat Enterprise Linux 8 (HVM), SSD Volume Type - ami-052c08d70def0ac62 (64-bit x86) / ami-0ad289a92ed067259 (64-bit Arm)
                  """
                  )
            x=int(input("Enter your choice: "))
            fs=''.join(s[x-1])
            fst ="aws ec2 run-instances --image-id "+fs+" --instance-type t2.micro --security-group-ids "+fsgid+" --key-name "+k
            os.system(fst)
        elif ch==2:
            lit='aws ec2 describe-instances --filters "Name=instance-type,Values=t2.micro" --query "Reservations[].Instances[].InstanceId"'
            os.system(lit)
        elif ch==3:    
            sz=input("Enter size of EBS volume you want to create : ")
            sebs="aws ec2 create-volume --size "+sz+" --availability-zone ap-south-1a --volume-type gp2"
            os.system(sebs)
        elif ch==4:
            iid=input("Enter instance id with which u want to attach : ")
            vid=input("Enter volume id which u want to attach : ")
            fatch="aws ec2 attach-volume --instance-id "+iid+" --volume-id "+vid+" --device /dev/sdf"
            os.system(fatch)
        else:
            ch=5
#Hadoop menu

#menu_hadoop()
# THIS FUNCTION HAS TO RUN INSIDE A DATANODE OF THE CLUSTER
def menu_hadoop():
       print(' ******************this is the hadoop section******************')
       choice=int(input("""
       \t\t\t1. View admin report \n 
       \t\t\t2. put a file into the cluster \n 
       \t\t\t3. delete a file from the cluster \n 
       \t\t\t4. read the file\n 
       \t\t\t5. go to the prev menu \n
       >>>"""))
       if choice== 1:
              view()
       elif choice==2:
              put()
       elif choice==3:
              delete()
       elif choice==4:
              read()
       elif choice==5:
              #call the parent menu function here
              print()
       else: 
              print('Invalid input, sorry try again')
def put():
       import subprocess as sp
       filename=input('Please enter the file name that you want to push to cluster \n >>>')
       output= sp.getstatusoutput("hadoop fs -put % s /"% filename)
       if output[0] == 0:
              print('Upload sucessfull')
       else:
              print('Some error occured')

def view():
       import subprocess as sp 
       filename= input('Please enter the file you want to read through \n >>>')
       output= sp.getstatusoutput("hadoop fs -cat % s /"% filename)
       if output[0] != 0:
              print('Some error occured.')

def read():
       import subprocess as sp
       filename=input('Please enter the file name that you want to read from the cluster \n >>>')
       output= sp.getstatusoutput("hadoop fs -cat /% s"% filename)
       if output[0] != 0:
              print('Some error occured')
       else:
              print(output)

def delete():
       import subprocess as sp
       filename=input('Please enter the file name that you want to remove from cluster \n >>>')
       output= sp.getstatusoutput("hadoop fs -rm /% s"% filename)
       if output[0] == 0:
              print('removal sucessfull')
       else:
              print('Some error occured')
#Docker menu

import os
import sys
def dock():
 def run(y):
  os.system(y)
 print("\t\t\t\tWelocme to docker menu")
 print("""
	Press 1 : To launch OS
	Press 2 : To see running OS
	Press 3 : To delete specific OS
	Press 4 : To stop specific OS
	Press 5 : To delete all OS
	Press 6 : To stop all OS
        Press 7 : To exit
	""")
 ch=input("Enter your choice : ")
 if int(ch) == 1:
  print("""\n
	 Press 1 : To launch Ubuntu
	 Press 2 : To launch Centos
	 Press 3 : To launch Fedora
	 """)
  ch1=input("Enter your choice : ")
  x=input("Enter no. of OS you want to launch : ")
  n=int(x)
  if int(ch1) == 1:
   print("""\n
	 Press 1 : To launch Ubuntu 20.10
	 Press 2 : To launch Ubuntu 18.04
	 Press 3 : To launch Ubuntu 16.04
	 """)
   ch2=input("Enter your choice : ")
   if int(ch2) == 1:
    for i in range(n):
     j=str(i+1)
     y=("docker run -it --name ubuntu% s ubuntu:20.10"% j)
     run(y)
    dock()
   elif int(ch2) == 2:
    for i in range(n):
     j=str(i+1)
     y=("docker run -it --name ubuntu% s ubuntu:18.04"% j)
     run(y)
    dock()
   elif int(ch2) == 3:
    for i in range(n):
     j=str(i+1)
     y=("docker run -it --name ubuntu% s ubuntu:16.04"% j)
     run(y)
    dock()
   else:
    print("Input not supported")
  elif int(ch1) == 2:
   print("""\n
	 Press 1 : To launch Centos 8
	 Press 2 : To launch Centos 7
	 Press 3 : To launch Centos 6
	 """)
   ch2=input("Enter your choice : ")
   if int(ch2) == 1:
    for i in range(n):
     j=str(i+1)
     y=("docker run -it --name cent% s centos:8"% j)
     run(y)
    dock()
   elif int(ch2) == 2:
    for i in range(n):
     j=str(i+1)
     y=("docker run -it --name cent% s centos:7"% j)
     run(y)
    dock()
   elif int(ch2) == 3:
    for i in range(n):
     j=str(i+1)
     y=("docker run -it --name cent% s centos:6"% j)
     run(y)
    dock()
   else:
    print("Input not supported")
  elif int(ch1) == 3:
   print("""\n
	 Press 1 : To launch Fedora 31
	 Press 2 : To launch Fedora 32
	 Press 3 : To launch Fedora latest
        """)
   ch2=input("Enter your choice : ")
   if int(ch2) == 1:
    for i in range(n):
     j=str(i+1)
     y=("docker run -it --name fed% s fedora:31"% j)
     run(y)
    dock()
   elif int(ch2) == 2:
    for i in range(n):
     j=str(i+1)
     y=("docker run -it --name fed% s fedora:32"% j)
     run(y)
    dock()
   elif int(ch2) == 3:
    for i in range(n):
     j=str(i+1)
     y=("docker run -it --name fed% s fedora:latest"% j)
     run(y)
    dock()
  else:
   print("Input not supported")
 elif int(ch) == 2:
  os.system("docker ps -a")
  dock()
 elif int(ch) == 3:
  name=str(input("Enter container name : "))
  y=("docker rm % s"%name)
  os.system(y)
  dock()
 elif int(ch) == 4:
  name=str(input("Enter container name : "))
  y=("docker stop % s"%name)
  os.system(y)
  dock()
 elif int(ch) == 5:
  os.system("docker rm $(docker ps -aq)")
  dock()
 elif int(ch) == 6:
  os.system("docker stop $(docker ps -aq)")
  dock()
 elif int(ch) == 7:
  sys.exit()
 else:
  print("Input not supported")

print("""\n
   Press 1 : For AWS
   Press 2 : For Hadoop
   Press 3 : For Docker
        """)
ch=input("Enter your choice : ")
if int(ch) == 1:
  menu_AWS()
elif int(ch) == 2:
  menu_hadoop()
elif int(ch) == 3:
 dock()
else:
  print("Input not supported")
