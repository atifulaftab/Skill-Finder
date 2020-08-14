# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 20:30:08 2020

@author: atifu
"""

def report_genarate(selected):
    f = open("SelectedCV.txt", "r+")
    for selection in selected:
        f.write(selection)
        f.write("\n")
    f.close()