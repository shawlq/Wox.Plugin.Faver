import logging

import time
date = time.strftime("%Y-%m-%d",time.localtime())

logging.basicConfig(level=logging.INFO,  
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                    datefmt='%a, %d %b %Y %H:%M:%S',  
                    filename=r'./logs/out_%s.log'%date,  
                    filemode='a+')

logger = logging.getLogger("faves") 