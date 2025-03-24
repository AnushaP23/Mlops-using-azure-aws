#this is used for logging purposes(tracking the exceution so we can point of errors easily)
import logging 
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), 'logs',LOG_FILE) #setting the path
os.makedirs(logs_path, exist_ok=True) #eventhough we have file it should keep on updating

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format =  "[%(asctime)s] %(lineno)d %(name)s - %(message)s",
    level = logging.INFO,

)
