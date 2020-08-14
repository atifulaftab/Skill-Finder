# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 18:27:28 2020

@author: atifu
"""

import os
from pdfToWords import pdfToWords
from extractSkill import extractSkill
from report_generate import report_genarate
def readPdfandMineSkill():
    no_of_pdf = 0
    competency = 0 
    foldername = input("Enter Folder Name: \t")
    selected = []
    my_keyword=[]
    noofskill=int(input("Enter no. of skills you want to check:\t"))
    for x in range(noofskill):
        my_keyword.append(input("Enter Skill:\t"))
    threshold=int(input("Enter threshold for cv slection:\t"))
    directory = os.path.join(".//"+foldername)
    for root,dirs,files in os.walk(directory):
        for file in files:
            if file.endswith(".pdf"):
                filename = file
                keywords = pdfToWords(file, filename,directory)
                competency=extractSkill(keywords, filename,my_keyword)
                no_of_pdf = no_of_pdf+1
                if competency >= threshold:
                    selected.append(filename)
    print("\n") 
    print("######Selected CV#####")
    for selection in selected:
            print(selection) 
    print("\n#######Generating Report#######\n")  
    report_genarate(selected,threshold)  
    print("Generation Completed!!!!")         
    return no_of_pdf