import logging

#color
class Logger:                                                                      
        HEADER = '\033[95m'                                                        
        OKBLUE = '\033[94m'                                                        
        OKGREEN = '\033[92m'                                                       
        WARNING = '\033[93m'                                                       
        FAIL = '\033[91m'                                                          
        ENDC = '\033[0m'


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                    datefmt='%Y %H:%M:%S',
                    filename='',
                    filemode='w')
def print_check_log(key,issec):
	if issec == 0:
		logging.info(key+' is security')
	if issec == 1:
		logging.warning(key+' no security')
	if issec == 2:
		logging.error(key+' no project')

def print_repaire_log(key):
	logging.critical(key+' repaired')
