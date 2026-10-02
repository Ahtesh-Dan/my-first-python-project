import logging
import os
folder_address = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(folder_address,"math_activity.log")
logging.basicConfig(filename=log_file, 
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)
try:
    answer = 50/0
    logging.info(f'if the answer is correct please save the in log file')
    
except Exception as e:
     logging.info(f"⚠️ ALERT: Ek error aaya jiska naam hai -> {e}")
print("Mission Complete! Check the 'math_activity.log' file in your folder.")