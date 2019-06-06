# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:58:08 2019

@author: HK067344
"""
#Put this file into any of your folder you want to organize and run it from the console or IDE of your choice.
#Make folders of the names same as Images,TextFiles and so on,the script is straightforward and easily understandable.
#Comment or ask in any case if you need clarification.
#Try to remove the SOftware field in the case of C drive for precaution.
import os
import shutil

fullpath = os.path.join
image_directory = "./Images"
text_files = "./TextFiles"
software_files = "./Software"
pdf_files = "./PDF"
count = 0
for (dirname, dirs, files) in os.walk('.'):
   for filename in files:
       source = fullpath(dirname, filename)
       
       if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg') :
           shutil.move(source, fullpath(image_directory, filename))
           count = count + 1
        if filename.endswith('.pdf')  :
           shutil.move(source, fullpath(pdf_files, filename))
           count = count + 1   
       if filename.endswith("txt"):
                shutil.move(source, fullpath(text_files, filename))   
       if filename.endswith(".exe") or filename.endswith(".jar"):
                shutil.move(source, fullpath(software_files, filename))            
print ('Files:', count)