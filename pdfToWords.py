# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 18:22:54 2020

@author: atifu
"""

import PyPDF2
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def pdfToWords(file,filename,directory):
    filereader = open(directory+"//"+filename,'rb')
    file = PyPDF2.PdfFileReader(filereader)
    num_pages = file.numPages
    count = 0
    text = ""
    while count < num_pages:
        page = file.getPage(count)
        count +=1
        text += page.extractText()
    if text != "":
       text = text
    else:
       text = textract.process(filename, method='tesseract', language='eng')
    
    tokens = word_tokenize(text)
    punctuations = ['(',')',';',':','[',']',',']
    stop_words = stopwords.words('english')
    keywords = [word for word in tokens if not word in stop_words and not word in punctuations]
    
    return keywords