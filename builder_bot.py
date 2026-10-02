import os 
import json
folder_address = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(folder_address,"company_data.json")
with open (json_file_path,"r") as file :
    data = json.load(file)
print("json Data load successfully!")
company = data["company_name"]
dept_list = data ["departments" ]
main_folder_path = os.path.join(folder_address,company)
os.makedirs(main_folder_path,exist_ok=True)
print(f"main HQ built Company:{company}")
for dept in dept_list :
    dept_path = os.path.join(main_folder_path,dept)
    os.makedirs(dept_path,exist_ok=True)
    print(f'Department created:{dept}')
print("___" * 40)
print("🚀 Automation Complete! Jaakar folder check kijiye.")
