import logging
import os
from datetime import datetime

LOG_FIlE=f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FIlE)
os.makedirs(logs_path,exist_ok=True)

logs_path_path=os.path.join(logs_path,LOG_FIlE)

logging.basicConfig(
    filename=logs_path_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info('logging has started')