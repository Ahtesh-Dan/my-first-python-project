import os 
import shutil
folder_address = os.path.dirname(os.path.abspath(__file__))
Target_folder = os.path.join(folder_address,"company_server")
junk_list=["backup_3","backup_4"]
for junk in junk_list:
    junk_path = os.path.join(Target_folder,junk)
    print(f"Bot started delete the folder: {junk}")
    if os.path.exists(junk_path):
        shutil.rmtree(junk_path)
        print(f'Bot Deleted the targeted Folder.')
    else:
        print("Targeted Folder not Found")