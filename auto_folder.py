import os
folder_address =os.path.dirname(os.path.abspath(__file__))
main_folder = os.path.join(folder_address,"clouds_backups")
for i in range (1,6):
    sub_folder_name = f"backup_{i}"
    final_path = os.path.join(main_folder,sub_folder_name)
    os.makedirs(final_path,exist_ok=True)
    print(f"✅ Ready: {sub_folder_name}")
print("-" * 50)
print("🏁 Mission Complete: Andar jaakar check kijiye, 5 folders ban chuke hain!")

    



