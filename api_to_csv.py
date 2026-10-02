import requests
import csv
import os
import logging
import time
folder_address=os.path.dirname(os.path.abspath(__file__))
log_file= os.path.join(folder_address,"scraper_acitivity.log")
logging.basicConfig(
    filename=log_file, 
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)
csv_file = os.path.join(folder_address,"live_jokes_data.csv")
logging.info("🚀 API to CSV Scraper Started!")
with open(csv_file, mode="w",newline="", encoding="utf-8") as file:
    writer=csv.writer(file)
    writer.writerow(["ID","setup","punchline"])
    for i in range(3):
        try:
            response = requests.get("https://official-joke-api.appspot.com/random_joke")
            if response.status_code == 200:
                live_data = response.json()
                writer.writerow([i+1, live_data['setup'], live_data['punchline']])
                logging.info(f"✅ Joke {i+1} saved to CSV!")
        except Exception as e:
            logging.error(f"⚠️ Error at attempt {i+1}: Internet Down! ({e})")
        time.sleep(2)
logging.info("🏁 Mission Complete!")
print(f"🔥 Success! Apni nayi 'live_jokes_data.csv' file check kijiye!")
                
    
            
                

           



