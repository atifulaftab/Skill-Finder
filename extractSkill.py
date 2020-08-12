# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 18:26:12 2020

@author: atifu
"""


import os

def extractSkill(keywords,filename,my_keyword):
    no_of_pdf=0
    competency=0
    final=0
    copy=[]
    print("###################{}#################".format(filename))
    for check_requirement in my_keyword:
        for pdf_words in keywords:
            if check_requirement == pdf_words:
                if len(copy)==0:
                    copy.append(pdf_words)    
                    competency=competency+1
                    print("Pdf {} has {}".format(filename,pdf_words))
                else:
                    for copies in copy:
                        if copies != pdf_words:
                            competency=competency+1
                            print("Pdf {} has {}".format(filename,pdf_words))
                            copy.append(pdf_words)
    print("Pdf {} has {} skill point".format(filename,competency))
    print("\n")