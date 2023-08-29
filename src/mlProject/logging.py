import logging
import os
from datetime import datetime


Log_file= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S_%')}.log"
Logs_path = os.path.join(os.getcwd(),"logs", Log_file)
os.makedirs(Logs_path,exist_ok=True)


LOG_FILE_PATH = os.path.join(Logs_path,Log_file)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
