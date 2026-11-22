import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)
log_path_file=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=log_path_file,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

#[%(asctime)s]= date and time of the log entry
# %(lineno)= line number from where the log entry was generated
# %(name)s = name of the logger that generated the log entry
# %(levelname)s = the severity level of the log entry (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)
# %(message)s= the actual log message provided by the application code