# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 18:27:28 2020

@author: atifu
"""

import os
from pdfToWords import pdfToWords
from extractSkill import extractSkill
def readPdfandMineSkill():
    no_of_pdf = 0
    foldername = input("Enter Folder Name: \t")
    my_keyword=[]
    noofskill=int(input("Enter no. of skills:\t"))
    for x in range(noofskill):
        my_keyword.append(input("Enter Skill:\t"))
    directory = os.path.join(".//"+foldername)
    for root,dirs,files in os.walk(directory):
        for file in files:
            if file.endswith(".pdf"):
                filename = file
                keywords = pdfToWords(file, filename,directory)
                extractSkill(keywords, filename,my_keyword)
                no_of_pdf = no_of_pdf+1
    return no_of_pdf