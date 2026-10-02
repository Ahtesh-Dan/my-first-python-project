import os
import shutil
folder_address = os.path.dirname(os.path.abspath(__file__))
Target_folder  = os.path.join(folder_address,"company_server")
junk_list = ["server_[depertments]", "server_['HR', 'IT', 'Finance']"]
for junk in junk_list:
    junk_path = os.path.join(Target_folder,junk)
    print(f"Bot started delete for folder: {junk}")
    if os.path.exists(junk):
        shutil.rmtree(junk)
    else:
        print(print("Target nahi mila."))    
        

    
  

    