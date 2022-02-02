# this file for get configuration from user.

import os
import sys
import logmodule
import configparser

# usage:
# if you're use defaultconfig thats load defaultconfig YOU CAN JUST ONE HEADER | LABEL | LINE 

config = configparser.ConfigParser()
def addconfig(header,headerlabel,headerline):
	config.add_section(header)
	config.set(header, headerlabel, headerline)
if os.path.exists('config.ini'):
	logmodule.log('.INI dosyaniz bulundu. ',1)
else:
	logmodule.log('.INI dosyaniz bulunamadi. ', 2)
	f = open("config.ini", "x")
	f.close()	
addconfig('tesseractOCR','tesseract','True')
addconfig('PaddleOCR','PaddlePaddle','False')
addconfig('EasyOCR','EasyOCR','False')
with open(r"config.ini", 'w') as configfile:
    config.write(configfile)