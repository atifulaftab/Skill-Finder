# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 20:30:08 2020

@author: atifu
"""

from datetime import datetime
import platform
import socket
import os

def report_genarate(selected,threshold,my_keyword):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.date()
    host_name=socket.gethostname()
    platform_name=platform.node()
    os_version=os.environ['COMPUTERNAME']
    file_name=str(current_date)+" and "+(now.strftime("%H %M %S"))
    f = open(file_name+".txt", "w")
    f.write("Skill Extractor 2.0.4\n")
    f.write("Generated on: {}\n".format(os_version))
    f.write("Skills to be considered: ")
    for skills in my_keyword:
        f.write(skills+", ")
    f.write("\n")
    f.write("Threshold for selection: {} %\n".format(threshold))
    f.write("\n############Selected CV#############\n")
    for selection in selected:
        f.write(selection)
        f.write("\n")
    f.write("\n")
    f.write("Generated at:{}  {}\n".format(current_date,current_time))
    f.close()