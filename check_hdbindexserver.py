#!/usr/bin/python

# Script created by: Luis Contreras
# Nagios Community Leader
# Email: lcontreras@nagios.com | luis.contreras.do@gmail.com
# Nagios Enterprise Website: www.nagios.com | www.nagios.org

# We only need this modules


import os, sys

# Daemon that belong to SAP HANA

daemon1=os.popen("sapcontrol -nr 00 -function GetProcessList | grep hdbindexserver | awk '{print $1}'").readline().strip()

# With original SAP HANA Command, we can check status of the process

status1=os.popen("sapcontrol -nr 00 -function GetProcessList | grep hdbindexserver | awk '{print $4}'").readline().strip()

# Checking actual process ID 

id1=os.popen("sapcontrol -nr 00 -function GetProcessList | grep hdbindexserver | awk '{print $11}'").readline().strip()


if (status1 == "GREEN," and daemon1 == "hdbindexserver,"):
	print "Process %s it's running in process ID : %s - process status : %s." % (daemon1, id1, status1)
        sys.exit(0)

if (status1 == "YELLOW," and daemon1 == "hdbindexserver,"):
        print "WARNING - Process %s is %s it's going up" % (daemon1, status1)
        sys.exit(1)

elif (status1 == "GRAY" and daemon1 == "hdbindexserver,"):
        print "CRITICAL - Process %s is %s it's not going to go up" % (daemon1, status1)
        sys.exit(2)
else:
        print "UNKNOWN - %s is %s .We can not identify process status" % (daemon1, status1)
        sys.exit(3)

