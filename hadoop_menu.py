def hadoop():

	import os

	os.system("tput setaf 3")
	print("\t\t\tWelcome to Hadoop menu!!")
	os.system("tput setaf 7")
	print("\t\t\t---------------------")

	print("\nEnter the required details:")
	nip=input("\nEnter your Namenode IP:")
	dip=input("\nEnter your Datanode IP:")
	print("\nNamenode:")
	print(nip)
	print("\nDatanode:")
	print(dip)


	while True:
		os.system("clear")
		print("""
		\n	
		Press 1 : To install Hadoop dependencies( jdk & hadoop)
		Press 2 : To check the version of hadoop and jdk
		Press 3 : To Configure namenode
		Press 4 : To format the service of namenode
		Press 5 : To start the service of namenode
		Press 6 : To check the report of hadoop
		Press 7 : To Configure datanode
		Press 8 : To start the service of datanode
		Press 9 : To check the report of hadoop
		Press 10 : exit
		""")

		ch = input("Enter ur choice:")
		print(ch)
		if int(ch)==1:
			os.system('ssh {} rpm -ivh jdk-8u171-linux-x64.rpm'.format(nip))
			os.system('ssh {} rpm -ivh jdk-8u171-linux-x64.rpm'.format(dip))
			print("--------------------------")
			print("\n\tJdk successfully installed in both nn & dn...")
			os.system('ssh {} rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force'.format(nip))
			os.system('ssh {} rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force'.format(dip))
			print("--------------------------")
			print("hadoop installed successfully in both nn & dn")
		elif int(ch)==2:
			print("\nIn Namenode")
			os.system("ssh {} hadoop version".format(nip))
			print("\nIn Datanode")
			os.system("ssh {} hadoop version".format(dip))
			print("\nIn Namenode:")
			os.system("ssh {} java -version".format(nip))
			print("\nIn Datanode:")
			os.system("ssh {} java -version".format(dip))

		elif int(ch)==3:
			
			os.system("ssh {} systemctl stop firewalld".format(nip))
			ndir = input("\n\t\tEnter directory name for namenode : ")
			print("\t\tConfiguring hdfs-site.xml file ............")
			os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/hdfs-site.xml")
			os.system("echo -e '\n<!-- Put site-specific property overrides in this file. -->' >> /root/hdfs-site.xml")
			os.system('echo -e "\n<configuration>" >> /root/hdfs-site.xml')
			os.system('echo -e "\n<property>" >> /root/hdfs-site.xml')
			os.system('echo -e "<name>dfs.name.dir</name>" >> /root/hdfs-site.xml')
			os.system('echo -e "<value>{}</value>" >> /root/hdfs-site.xml'.format(ndir))
			os.system('echo -e "</property>" >> /root/hdfs-site.xml')
			os.system('echo -e "\n</configuration>" >> /root/hdfs-site.xml')
			os.system('scp /root/hdfs-site.xml {}:/etc/hadoop'.format(nip))
			print()
			print()
			
			print("\t\tConfiguring core-site.xml file ...........")
			os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
			os.system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
			os.system('echo -e "\n<configuration>" >> /root/core-site.xml')
			os.system('echo -e "\n<property>" >> /root/core-site.xml')
			os.system('echo -e "<name>fs.default.name</name>" >> /root/core-site.xml')
			os.system('echo -e "<value>hdfs://0.0.0.0:9001</value>" >> /root/core-site.xml'.format(nip))
			os.system('echo -e "</property>" >> /root/core-site.xml')
			os.system('echo -e "\n</configuration>" >> /root/core-site.xml')
			os.system('scp /root/core-site.xml {}:/etc/hadoop'.format(nip))
		elif int(ch) ==4:
			os.system('ssh {} hadoop namenode -format'.format(nip))
			
		elif int(ch) == 5:
			print("\n\n\t\t\t\t\tstarting hadoop namenode services .........")
			os.system('ssh {} hadoop-daemon.sh start namenode'.format(nip))
			print()
		elif int(ch) == 6:
			os.system('ssh {} hadoop dfsadmin -report'.format(nip))
			print()

		
		elif int(ch)==7:
			
			os.system("ssh {} systemctl stop firewalld".format(dip))
			dir = input("\n\t\tEnter directory name for datanode : ")
			print("\t\tConfiguring hdfs-site.xml file ............")
			os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/hdfs-site.xml")
			os.system("echo -e '\n<!-- Put site-specific property overrides in this file. -->' >> /root/hdfs-site.xml")
			os.system('echo -e "\n<configuration>" >> /root/hdfs-site.xml')
			os.system('echo -e "\n<property>" >> /root/hdfs-site.xml')
			os.system('echo -e "<name>dfs.data.dir</name>" >> /root/hdfs-site.xml')
			os.system('echo -e "<value>{}</value>" >> /root/hdfs-site.xml'.format(dir))
			os.system('echo -e "</property>" >> /root/hdfs-site.xml')
			os.system('echo -e "\n</configuration>" >> /root/hdfs-site.xml')
			os.system('scp /root/hdfs-site.xml {}:/etc/hadoop'.format(dip))
			print()
			print()
			nnip = input("Enter Name Node IP :")
			print("\t\tConfiguring core-site.xml file ...........")
			os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
			os.system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
			os.system('echo -e "\n<configuration>" >> /root/core-site.xml')
			os.system('echo -e "\n<property>" >> /root/core-site.xml')
			os.system('echo -e "<name>fs.default.name</name>" >> /root/core-site.xml')
			os.system('echo -e "<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(nnip))
			os.system('echo -e "</property>" >> /root/core-site.xml')
			os.system('echo -e "\n</configuration>" >> /root/core-site.xml')
			os.system('scp /root/core-site.xml {}:/etc/hadoop'.format(dip))
		elif int(ch) == 8:
			print("\n\n\t\t\t\t\tstarting hadoop data node services .........")
			os.system('ssh {} hadoop-daemon.sh start datanode'.format(dip))
			print()
		elif int(ch) == 9:
			os.system('ssh {} hadoop dfsadmin -report'.format(dip))
			print()
			
		elif int(ch)==10:
			exit()
		else:
			print("not supported")
		
		input("\nplz enter to cont...")
		


