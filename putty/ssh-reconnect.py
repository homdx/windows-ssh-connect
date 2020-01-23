import subprocess
from tendo import singleton
import time

me = singleton.SingleInstance() #exits if another instance exists

while True:
 print("Starting putty session...")
 subprocess.call('"putty.exe" -load "profile" user@ip_dns')
 print("Putty session closed... restarting...")
 time.sleep(5)   #sleep to avoid infinitely fast restarting if no connection is present
