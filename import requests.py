import requests
import time
import os
import logging
folder_address = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(folder_address,"bot_activity.log")
logging.basicConfig(filename=log_file,level=logging.INFO,format = "%(asctime)s-%(levelname)s-%(message)s")
logging.info("🚀 Turbo Scraper Started working...")
file_address = os.path.join(folder_address, "jokes_data.txt")

with open(file_address, "a", encoding="utf-8") as file:
    for i in range(3):

        # Yahan se humara SHIELD shuru hota hai
        try:

            # Notice kijiye yeh line 'try:' ke aage (right side) khiski hui hai
            response = requests.get("https://official-joke-api.appspot.com/random_joke")

            
            if response.status_code == 200:

                live_data = response.json()

                
                file.write(f"Data #{i+1}\n")
                file.write(f"Setup: {live_data['setup']}\n")
                file.write(f"Punchline: {live_data['punchline']}\n")
                file.write("-" * 30 + "\n")
                logging.info(f"✅ Joke {i+1} saved successfully!")
                logging.info(f"✅ Joke {i+1} saved successfully!")
                
        # Yahan humara SHIELD khatam hota hai aur ERROR catch hota hai        
        except Exception as e:
            # Notice kijiye yeh line 'except:' ke aage (right side) khiski hui hai
          logging.error(f"⚠️ Connection error at attempt {i+1}! Internet down. ({e})")
        
        # Time wali line try-except ke bahar par loop ke andar hai
        time.sleep(2)
    logging.info(f"🏁 Scraping Complete! Data saved at: {file_address}")


print("Mission Complete! Check the 'bot_activity.log' file in your folder.")