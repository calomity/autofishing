# this file for log infos errors etc.

import logging
import sys
import os
import shutil
from datetime import datetime

# usage:
# logmodule.log('Zort',1)
# logmodule.log('Zort',2)
# logmodule.log('Zort',3)
# logmodule.log('Zort',4)
# logmodule.clearlogs('log/')

now = datetime.now().strftime("%Y_%m_%d %H-%M-%S")
logfile1 = now + 'logs'
if os.path.exists('log'):
	logfile2 = 'log/' + logfile1
	os.mkdir(logfile2)
	handler = logging.FileHandler(logfile2 + '/logs.log')
else:
	os.mkdir('log')
	logfile2 = 'log/' + logfile1
	os.mkdir(logfile2)

def log(message,a):
	logger = logging.getLogger()
	logger.setLevel(logging.INFO)
	formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
	handler = logging.FileHandler(logfile2 + '/logs.log')
	handler.setFormatter(formatter)
	logger.addHandler(handler)
	if a == 1:
		logger.info(message)
	if a == 2:
		logger.error(message)
	if a == 3:
		logger.warning(message)
	if a == 4:
		logger.debug(message)
	logging.shutdown()	

def clearlogs(path):
	for filename in os.listdir(path):
	    filepath = os.path.join(path, filename)
	    try:
	        shutil.rmtree(filepath)
	    except OSError:
	        os.remove(filepath)