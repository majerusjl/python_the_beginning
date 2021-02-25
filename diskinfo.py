# Show hard drives under Windows 10 and identify which disk the OS is booted up on.
import subprocess, wmi

def diskcount():
   w = wmi.WMI()
   x = 0
   for drive in w.Win32_DiskDrive():
        x+=1
   return(x)

num = diskcount()
for i in range(num):
   print(" ")
   disks = subprocess.Popen(['powershell', 'get-disk {} | format-list model, isboot'.format(i)], stdout=subprocess.PIPE).communicate()[0]
   print(disks.strip().decode('utf-8'))
   print(" ")
